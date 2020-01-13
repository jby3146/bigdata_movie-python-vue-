from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import create_profile
from django.contrib.auth.models import User
from api.models import Profile
from api.serializers import ProfileSerializer
from django.db import connection

#### 알고리즘 ####
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
#################

@api_view(['POST','GET'])
def signup_many(request):
    if request.method == 'GET':
        # id = request.GET.get('id', request.GET.get('movie_id', None))
        id = request.GET.get('id', None)
        gender = request.GET.get('gender', None)
        occupation = request.GET.get('occupation', None)
        age = request.GET.get('age',None)
        sort = request.GET.get('sort',None)
        users = Profile.objects.all()

        if id:
            #### 알고리즘 - 유사 유저 ####
            li = list()
            idx1 = 0

            for u in users:
                uid = u.id
                obj = usermovieSeen_sql(uid)

                seenMovie = ''
                for i in range( len(obj) ) :
                    seenMovie += str(obj[i]['mid']) + " "
                seenMovie = seenMovie.strip()

                uinfo = ''
                ugender = ''
                ujob = ''

                user = users.filter(pk=uid)
                for u in user:
                    uinfo += u.occupation + ' ' + u.gender
                    ugender = u.gender
                    ujob = u.occupation

                uinfo += ' ' + seenMovie

                li.append({'uid' : uid, 'idx' : idx1, 'info' : uinfo})
                idx1 += 1

            df = pd.DataFrame(li)
            cv = CountVectorizer()
            count_matrix = cv.fit_transform(df['info'])
            cosine_sim = cosine_similarity(count_matrix)
            user_index = int(id) - 1
            similar_users = list(enumerate(cosine_sim[user_index]))
            sorted_similar_users = sorted(similar_users, key=lambda x:x[1],reverse=True)[1:]
            print(sorted_similar_users)

            uidlist = ''
            i=0
            for element in sorted_similar_users:
                i = i + 1
                if i != 5 :
                    uidlist += str(li[ element[0] ]['uid']) + "|"
                else :
                    uidlist += str(li[ element[0] ]['uid'])
                if i >= 5:
                    break
            ############################

            users= users.filter(pk=id)
            users.update( uidlist=uidlist )
        if gender:
            users = users.filter(gender__icontains=gender)

        #rating 순
        if(sort == '1'):
            users = sorted(users, key=lambda user: user.age,reverse=True)

        serializer = ProfileSerializer(users, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


    if request.method == 'POST':
        profileDB = Profile.objects.all()
        profileDB.delete()
        userDB = User.objects.all()
        userDB.delete()
        profiles = request.data.get('profiles', None)

        for profile in profiles:
            id = profile.get('id', None)
            username = profile.get('username', None)
            password = profile.get('password', None)
            age = profile.get('age', None)
            occupation = profile.get('occupation', None)
            gender = profile.get('gender', None)

            create_profile(id=id, username=username, password=password, age=age,
                           occupation=occupation, gender=gender, uidlist='')

        return Response(status=status.HTTP_201_CREATED)



def dictfetchall(cursor):
  desc = cursor.description
  return [
          dict(zip([col[0] for col in desc], row))
          for row in cursor.fetchall()
  ]

###### 유사 유저 SQL 부분 ######

def usermovieSeen_sql(uid):
    cursor = connection.cursor()
    cursor.execute("SELECT movieid_id mid FROM api_rating WHERE userid_id = %s", [uid])
    row = dictfetchall(cursor)
    return row

###############################

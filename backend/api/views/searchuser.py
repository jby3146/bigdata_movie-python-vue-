from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import create_profile
from django.contrib.auth.models import User
from api.models import Profile
from api.serializers import ProfileSerializer
from django.db import connection
from api.models import Rating

@api_view(['POST'])
def user_search(request): 
    if request.method == 'POST':
        rdata = request.data["params"]
        movieid = rdata['movieid']
        username = rdata['username']
        user = User.objects.all().filter(username= username)
        uid = 0
        for u in user.values_list():
            uid = int(u[0])

        rating = searchrating_sql(movieid,uid)

        if len(rating)>0 :
            searchuser = {'movieid':movieid,'rating':rating[0]['rating'],'userid':uid}
            return Response(data=searchuser,status=status.HTTP_201_CREATED)
        else :
            return Response(data={'movieid':"None"})


def searchrating_sql(movieid, userid):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM api_rating WHERE movieid_id=%s and userid_id=%s",[movieid, userid])
    row = dictfetchall(cursor)
    return row

def dictfetchall(cursor):
  desc = cursor.description
  return [
          dict(zip([col[0] for col in desc], row))
          for row in cursor.fetchall()
  ]
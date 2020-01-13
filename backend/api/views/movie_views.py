from rest_framework import status
from rest_framework.decorators import api_view
from api.models import Movie , Profile, Rating
from api.serializers import MovieSerializer
from rest_framework.response import Response
from django.db import connection

#### 알고리즘 ####
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
#################

@api_view(['GET', 'POST', 'DELETE'])
def movies(request):
    if request.method == 'GET':
        id = request.GET.get('id', request.GET.get('movie_id', None))
        title = request.GET.get('title', None)
        genres = request.GET.get('genres',None)
        sort = request.GET.get('sort',None)
        sel = request.GET.get('sel',None)
        selGender = request.GET.get('selGender',None)
        selAge = request.GET.get('selAge',None)
        selOccupation = request.GET.get('selOccupation',None)
        counting = request.GET.get('counting', None)
        movies = Movie.objects.all()
        ratings = Rating.objects.all()
        if id:
            #### 알고리즘 - 유사 영화 ####
            li = list()
            mlist = ''

            idx1 = 0
            for m in movies :
                gen = m.genres.split('|')
                tmp = ' '
                for s in gen :
                    tmp += s + ' '
                tmp = tmp.strip()

                li.append({'title' : m.title, 'idx' : idx1, 'genres' : tmp})
                idx1 += 1

            df = pd.DataFrame(li)

            cv = CountVectorizer()
            count_matrix = cv.fit_transform(df['genres'])

            cosine_sim = cosine_similarity(count_matrix)

            #### 클릭한 영화의 제목 찾기 ####
            ms = Movie.objects.all().filter(id=id)
            mtitle = ''
            for m in ms :
                mtitle = m.title

            movie_user_likes = mtitle
            movie_index = get_index_from_title(df, movie_user_likes)
            similar_movies = list(enumerate(cosine_sim[movie_index]))

            sorted_similar_movies = sorted(similar_movies, key=lambda x:x[1],reverse=True)[1:]

            i=0
            for element in sorted_similar_movies:
                i = i+1
                if i != 5 :
                    mlist += get_title_from_index(df, element[0]) + "|"
                else :
                    mlist += get_title_from_index(df, element[0])
                if i>=5:
                    break
            ############################
            movies = movies.filter(pk=id)
            movies.update( mlist=mlist )
        if title:
            movies = movies.filter(title__icontains=title)
        if genres:
            movies = movies.filter(genres__icontains=genres)

        # 성별 검색
        if sel == '1' :
            obj = usermovieGender_sql(selGender, int(counting))
            size = 0
            repeat = 0
            if( len(obj) > 5 ) :
                repeat = 5
            elif len(obj) == 0 :
                repeat = 1
            else :
                repeat = len(obj)

            for idx in range( repeat ) :
                if( len(obj) == 0 ) :
                    movies = []
                    break
                if size == 0:
                    movies = movies.filter( pk=obj[0]['m_id'] )
                    movies.update( counting=obj[idx]['cnt'] )
                    size = size + 1
                else :
                    m = Movie.objects.filter(pk=obj[idx]['m_id'])
                    m.update(counting=obj[idx]['cnt'])
                    movies = movies.union(m)
            movies = sorted(movies, key=lambda movie: movie.counting, reverse=True)
        # 나이 검색
        if sel == '2' :
            obj = usermovieAge_sql(selAge, int(counting))
            size = 0
            repeat = 0
            if( len(obj) > 5 ) :
                repeat = 5
            elif len(obj) == 0 :
                repeat = 1
            else :
                repeat = len(obj)

            for idx in range( repeat ) :
                if( len(obj) == 0 ) :
                    movies = []
                    break
                if size == 0:
                    movies = movies.filter( pk=obj[0]['m_id'] )
                    movies.update( counting=obj[idx]['cnt'] )
                    size = size + 1
                else :
                    m = Movie.objects.filter(pk=obj[idx]['m_id'])
                    m.update(counting=obj[idx]['cnt'])
                    movies = movies.union(m)
            movies = sorted(movies, key=lambda movie: movie.counting, reverse=True)
        # 직업 검색
        if sel == '3' :
            obj = usermovieOccupation_sql(selOccupation, int(counting))
            size = 0
            repeat = 0
            if( len(obj) > 5 ) :
                repeat = 5
            elif len(obj) == 0 :
                repeat = 1
            else :
                repeat = len(obj)

            for idx in range( repeat ) :
                if( len(obj) == 0 ) :
                    movies = []
                    break
                if size == 0:
                    movies = movies.filter( pk=obj[0]['m_id'] )
                    movies.update( counting=obj[idx]['cnt'] )
                    size = size + 1
                else :
                    m = Movie.objects.filter(pk=obj[idx]['m_id'])
                    m.update(counting=obj[idx]['cnt'])
                    movies = movies.union(m)
            movies = sorted(movies, key=lambda movie: movie.counting, reverse=True)

        #rating 순
        if(sort == '1'):
            movies = sorted(movies, key=lambda movie: movie.ratings / movie.viewCnt if movie.viewCnt != 0 else 0,reverse=True)
        if(sort == '2'):
            movies = sorted(movies, key=lambda movie: movie.viewCnt,reverse=True)

        serializer = MovieSerializer(movies, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    if request.method == 'DELETE':
        movie = Movie.objects.all()
        movie.delete()
        return Response(status=status.HTTP_200_OK)

    if request.method == 'POST':
        movieDb = Movie.objects.all()
        movieDb.delete()
        movies = request.data.get('movies', None)

        for movie in movies:
            id = movie.get('id', None)
            title = movie.get('title', None)
            genres = movie.get('genres', None)
            ratings = movie.get('ratings', None)
            viewCnt = movie.get('viewCnt', None)
            imgpath = movie.get('imgpath', None)
            overview = movie.get('overview', None)
            production_companies = movie.get('production_companies', None)
            production_countries = movie.get('production_countries', None)
            runtime = movie.get('runtime', None)

            Movie(id=id, title=title, ratings=ratings, viewCnt=viewCnt, genres='|'.join(genres), counting=0, mlist='', imgpath=imgpath, overview= overview,production_companies=production_companies, production_countries=production_countries ,runtime=runtime).save()

        return Response(status=status.HTTP_200_OK)

def usermovieGender_sql(gender, cnt):
  cursor = connection.cursor()
  cursor.execute("SELECT m.id as m_id, COUNT(*) as cnt FROM api_movie m, api_rating r, api_profile u WHERE m.id = r.movieid_id and u.id = r.userid_id and u.gender = %s GROUP BY m.id HAVING cnt > %s ORDER BY cnt desc", [gender, cnt])
  row = dictfetchall(cursor)
  return row

def usermovieAge_sql(age, cnt):
  cursor = connection.cursor()
  cursor.execute("SELECT m.id as m_id, COUNT(*) as cnt FROM api_movie m, api_rating r, api_profile u WHERE m.id = r.movieid_id and u.id = r.userid_id and u.age = %s GROUP BY m.id HAVING cnt > %s ORDER BY cnt desc",[age, cnt])
  row = dictfetchall(cursor)
  return row

def usermovieOccupation_sql(occupation, cnt):
  cursor = connection.cursor()
  cursor.execute("SELECT m.id as m_id, COUNT(*) as cnt FROM api_movie m, api_rating r, api_profile u WHERE m.id = r.movieid_id and u.id = r.userid_id and u.occupation = %s GROUP BY m.id HAVING cnt > %s ORDER BY cnt desc",[occupation, cnt])
  row = dictfetchall(cursor)
  return row

def dictfetchall(cursor):
  desc = cursor.description
  return [
          dict(zip([col[0] for col in desc], row))
          for row in cursor.fetchall()
  ]

##### 유사 영화 - 알고리즘 부분 #####
def get_title_from_index(df, idx):
    return df[df.idx == idx]["title"].values[0]

def get_index_from_title(df, title):
    return df[df.title == title]["idx"].values[0]
###################################

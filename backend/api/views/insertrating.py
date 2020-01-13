from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import create_profile
from django.contrib.auth.models import User
from api.models import Movie , Profile, Rating
from api.serializers import ProfileSerializer
from django.db import connection
from api.models import Rating

@api_view(['POST'])
def rating_insert(request): 
    if request.method == 'POST':
        rdata = request.data["params"]
        statuses = rdata['status']
        movieid = rdata['movieid']
        username = rdata['username']
        rating = rdata['rating']
        user = User.objects.all().filter(username= username)
        uid = 0
        for u in user.values_list():
            uid = int(u[0])
        sql_status = 0
        check_data=None
        before_rating = searchrating_sql(movieid,uid)
        movie_data = search_movie_sql(movieid)
        before_viewcnt = movie_data[0]['viewCnt']
        temp_ratings = 0
        temp_viewcnt = before_viewcnt
        if statuses==False :
            insert_sql(movieid, uid, rating)
            check_data = searchrating_sql(movieid,uid)
        else :
            update_sql(movieid, uid, rating)
            check_data = searchrating_sql(movieid,uid)
        
        sql_status = check_data[0]['rating']
        if len(before_rating)>0 :
            temp_ratings = movie_data[0]['ratings']-before_rating[0]['rating']+sql_status
        else :
            temp_ratings = movie_data[0]['ratings']+sql_status
            temp_viewcnt = before_viewcnt+1
        if int(sql_status)==int(rating) :
            update_movie_sql(movieid,temp_ratings,temp_viewcnt)
            return Response(data={'insert':'success'})
        else :
            return Response(data={'insert':'fail'})

def search_movie_sql(movieid):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM api_movie WHERE id=%s", [movieid])
    row = dictfetchall(cursor)
    return row


def update_movie_sql(movieid,ratings,viewCnt):
    cursor = connection.cursor()
    cursor.execute("UPDATE api_movie SET ratings=%s, viewCnt=%s WHERE id=%s",[ratings, viewCnt, movieid])
    row = dictfetchall(cursor)
    return row

def searchrating_sql(movieid, userid):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM api_rating WHERE movieid_id=%s and userid_id=%s", [movieid, userid])
    row = dictfetchall(cursor)
    return row

def insert_sql(movieid, userid,rating):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO api_rating(rating, movietitle, movieid_id, userid_id) VALUES (%s, %s, %s, %s)",[rating," ", movieid, userid])
    row = dictfetchall(cursor)
    return row

def update_sql(movieid, userid, rating):
    cursor = connection.cursor()
    cursor.execute("UPDATE api_rating SET rating=%s WHERE userid_id=%s and movieid_id=%s",[rating, userid, movieid])
    row = dictfetchall(cursor)
    return row


def dictfetchall(cursor):
  desc = cursor.description
  return [
          dict(zip([col[0] for col in desc], row))
          for row in cursor.fetchall()
  ]
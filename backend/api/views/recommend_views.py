import pandas as pd
import numpy as np
import sqlite3
import itertools
from scipy.sparse import csr_matrix
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.mixture import GaussianMixture
from sklearn.metrics import silhouette_samples, silhouette_score, mean_squared_error
from rest_framework import status
from rest_framework.decorators import api_view
from api.models import Movie, Profile, Rating, Clustering
from api.serializers import MovieSerializer, ClusteringSerializer
from rest_framework.response import Response
from django.db import connection
from django.forms import model_to_dict


@api_view(['GET','POST'])
def recommend(request):

    if request.method == 'GET':
        user_id = request.GET.get('id', None)
        movies = pd.DataFrame(list(Movie.objects.all().values('id','title'))) 
        movies.columns = ['movieid', 'title']
        ratings = pd.DataFrame(list(Rating.objects.all().values('userid','movieid','rating')))
        ratings_title = pd.merge(ratings, movies[['movieid', 'title']], on='movieid' )

        user_movie_ratings =  pd.pivot_table(ratings_title, index='userid', columns= 'title', values='rating')
        user_movie_ratings = user_movie_ratings.reset_index()
        clusters = pd.DataFrame(list(Clustering.objects.all().values('group'))) 
        clustered = pd.concat([user_movie_ratings, clusters], axis=1)

        cluster = Clustering.objects.all().filter(id = user_id)
        cluster_number = cluster[0].group
        
        # 같은 클러스터 부르기
        cluster = clustered[clustered.group == cluster_number].drop(['group'], axis=1)
        print(cluster)
        # 유저의 ratings을 다 가져온다.
        user_2_ratings  = cluster.loc[int(user_id), :]
        # 유저가 보지 않은 영화를 가져온다.
        user_2_unrated_movies =  user_2_ratings[user_2_ratings.isnull()]
        # 그 영화의 다른 유저들의 평균을 가져온다
        avg_ratings = pd.concat([user_2_unrated_movies, cluster.mean()], axis=1, join='inner').loc[:,0]
        print(avg_ratings)
        # 정렬 5개
        avg_ratings = avg_ratings.sort_values(ascending=False)[:6]
        movies = avg_ratings.index
        cnt = 0
        recommend_movies = Movie.objects.all().filter(id=-1)
        for movie in movies:
            print(movie)
            cnt+=1
            m = Movie.objects.all().filter(title = movie)
            recommend_movies = recommend_movies.union(m)

        serializer = MovieSerializer(recommend_movies, many=True)
        
        return Response(data=serializer.data, status=status.HTTP_200_OK)


    ## 포스트 하면 db.sqlite3에 있는 것 클러스터링 정보 갱신 
    if request.method == 'POST':

        cluster = request.data["params"]
        cluster_type = cluster["cluster"]
        # 클러스터 수
        cluster_n = cluster["number"]

        movies = pd.DataFrame(list(Movie.objects.all().values('id','title'))) 
        movies.columns = ['movieid', 'title']
        ratings = pd.DataFrame(list(Rating.objects.all().values('userid','movieid','rating')))
        ratings_title = pd.merge(ratings, movies[['movieid', 'title']], on='movieid' )
        ##가장 값이 많은 상위 1000개 데이터만 가져온다
        user_movie_ratings =  pd.pivot_table(ratings_title, index='userid', columns= 'title', values='rating')
        #most_rated_movies_1k = get_most_rated_movies(user_movie_ratings, 1000)
        #sparse_ratings = csr_matrix(pd.SparseDataFrame(most_rated_movies_1k).to_coo())
        sparse_ratings = csr_matrix(pd.SparseDataFrame(user_movie_ratings).to_coo())
        clustering = ""
        # 클러스터링
        print(sparse_ratings)
        con = sqlite3.connect("db.sqlite3")
        if cluster_type :
            if cluster_type == 1 :
                clustering = KMeans(n_clusters=cluster_n, algorithm='full').fit_predict(sparse_ratings)
            if cluster_type == 2 :
                clustering = AgglomerativeClustering(n_clusters=cluster_n, linkage='ward').fit_predict(sparse_ratings.toarray())
            if cluster_type == 3 : 
                clustering = GaussianMixture(n_components=cluster_n, covariance_type="full").fit_predict(sparse_ratings.toarray())
        
    
        clustered = pd.concat([user_movie_ratings.reset_index(), pd.DataFrame({'group':clustering})], axis=1)
        clustered = clustered[['userid','group']]
        print(clustered)
        clustered = clustered.fillna('')

        clustered.to_sql('cluster', con, if_exists="replace")
        con.close()
        
        '''
        kmeans = KMeans(n_clusters=cluster_n, algorithm='full').fit_predict(sparse_ratings)
        Hierarchical = AgglomerativeClustering(n_clusters=cluster_n, linkage='ward').fit_predict(sparse_ratings.toarray())
        EM = GaussianMixture(n_components=cluster_n, covariance_type="full").fit_predict(sparse_ratings.toarray())
        
        clusters = [kmeans,Hierarchical,EM]
        clustersStr = ['kmeans','Hierarchical','EM']

        # db에 저장
        con = sqlite3.connect("db.sqlite3")
        for i in range(0,3):
            clustered = pd.concat([most_rated_movies_1k.reset_index(), pd.DataFrame({'group':clusters[i]})], axis=1)
            clustered = clustered.fillna('')
            clustered.to_sql(clustersStr[i], con, if_exists="replace")
        con.close()
        '''
        con = sqlite3.connect("db.sqlite3")
        cur = con.cursor()
        serializer = ''
        if cluster :
            cur.execute("select * from cluster")

            rows = cur.fetchall()
            cnt = 0
            for row in rows:
                if(cnt == len(rows)-1):
                    break
                userid = int(row[1])
                group = int(row[-1])
                profile = list(Profile.objects.filter(user_id = userid).values())
                print(profile[0])
                print(profile[0]['user_id'])

                Clustering(id = int(profile[0]['user_id']),occupation=profile[0]['occupation'], gender=profile[0]['gender'],age=int(profile[0]['age']),group=group ).save()
                cnt = cnt+1
            clusters = Clustering.objects.all()
            con.close()
            serializer = ClusteringSerializer(clusters, many=True)
            
        return Response(data=serializer.data, status=status.HTTP_200_OK)

def clustering_errors(k, data):
    kmeans = KMeans(n_clusters=k).fit(data)
    predictions = kmeans.predict(data)
    silhouette_avg = silhouette_score(data, predictions)
    return silhouette_avg

def sparse_clustering_errors(k, data):
    kmeans = KMeans(n_clusters=k).fit(data)
    predictions = kmeans.predict(data)
    cluster_centers = kmeans.cluster_centers_
    errors = [mean_squared_error(row, cluster_centers[cluster]) for row, cluster in zip(data, predictions)]
    return sum(errors)

def get_most_rated_movies(user_movie_ratings, max_number_of_movies):
    # 1- Count
    user_movie_ratings = user_movie_ratings.append(user_movie_ratings.count(), ignore_index=True)
    # 2- sort
    user_movie_ratings_sorted = user_movie_ratings.sort_values(len(user_movie_ratings)-1, axis=1, ascending=False)
    user_movie_ratings_sorted = user_movie_ratings_sorted.drop(user_movie_ratings_sorted.tail(1).index)
    # 3- slice
    most_rated_movies = user_movie_ratings_sorted.iloc[:, :max_number_of_movies]
    return most_rated_movies

def get_users_who_rate_the_most(most_rated_movies, max_number_of_movies):
    # Get most voting users
    # 1- Count
    most_rated_movies['counts'] = pd.Series(most_rated_movies.count(axis=1))
    # 2- Sort
    most_rated_movies_users = most_rated_movies.sort_values('counts', ascending=False)
    # 3- Slice
    most_rated_movies_users_selection = most_rated_movies_users.iloc[:max_number_of_movies, :]
    most_rated_movies_users_selection = most_rated_movies_users_selection.drop(['counts'], axis=1)
    
    return most_rated_movies_users_selection

def sort_by_rating_density(user_movie_ratings, n_movies, n_users):
    most_rated_movies = get_most_rated_movies(user_movie_ratings, n_movies)
    most_rated_movies = get_users_who_rate_the_most(most_rated_movies, n_users)
    return most_rated_movies
    
    
def bias_genre_rating_dataset(genre_ratings, score_limit_1, score_limit_2):
    biased_dataset = genre_ratings[((genre_ratings['avg_romance_rating'] < score_limit_1 - 0.2) & (genre_ratings['avg_scifi_rating'] > score_limit_2)) | ((genre_ratings['avg_scifi_rating'] < score_limit_1) & (genre_ratings['avg_romance_rating'] > score_limit_2))]
    biased_dataset = pd.concat([biased_dataset[:300], genre_ratings[:2]])
    biased_dataset = pd.DataFrame(biased_dataset.to_records())
    return biased_dataset

'''
  if request.method == 'GET':
        cluster = request.GET.get('cluster', None)
        recommend = request.GET.get('recommend', None)
        con = sqlite3.connect("db.sqlite3")
        cur = con.cursor()
        serializer = ''
        movieDb = Clustering.objects.all()
        movieDb.delete()
        if cluster :
            if cluster == '1' :
                #df = pd.read_sql("SELECT * From kmeans" , con = con)
                cur.execute("select * from kmeans")
            if cluster == '2' :
                #df = pd.read_sql("SELECT * From Hierarchical", con = con)
                cur.execute("select * from Hierarchical")
            if cluster == '3' : 
                #df = pd.read_sql("SELECT * From EM", con = con)
                cur.execute("select * from EM")
            
            #print(df)
            rows = cur.fetchall()
            cnt = 0
            for row in rows:
                if(cnt == len(rows)-1):
                    break
                userid = int(row[0])+2
                group = int(row[-1])
                profile = list(Profile.objects.filter(user_id = userid).values())
                print(profile[0])
                print(profile[0]['user_id'])

                Clustering(id = int(profile[0]['user_id']),occupation=profile[0]['occupation'], gender=profile[0]['gender'],age=int(profile[0]['age']),group=group ).save()
                cnt = cnt+1
            clusters = Clustering.objects.all()
            con.close()
            serializer = ClusteringSerializer(clusters, many=True)
            
        if recommend :

            return
        
        return Response(data=serializer.data, status=status.HTTP_200_OK)
'''
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
from api.serializers import MovieSerializer, ClustringSerializer
from rest_framework.response import Response
from django.db import connection


@api_view(['GET','POST'])
def ratings(request):

 if request.method == 'POST':
        movies = pd.read_csv(
            '../data/movies.dat',
            sep='::', engine='python',
            names=['movieid', 'title', 'genres'],
        )

        ratings = pd.read_csv(
            '../data/ratings.dat',
            sep='::', engine='python',
            names=['userid','movieid','rating','time'],
        )
        #DB에 저장된거로 하자
        ratings_title = pd.merge(ratings, movies[['movieid', 'title']], on='movieid' )

        ##가장 값이 많은 상위 1000개 데이터만 가져온다
        user_movie_ratings =  pd.pivot_table(ratings_title, index='userid', columns= 'title', values='rating')
        most_rated_movies_1k = get_most_rated_movies(user_movie_ratings, 300)

        #이것이 오류 난다면 pandas 업데이트
        sparse_ratings = csr_matrix(pd.SparseDataFrame(most_rated_movies_1k).to_coo())
        cluster_n = 20
        # 20 clusters
        kmeans = KMeans(n_clusters=cluster_n, algorithm='full').fit_predict(sparse_ratings)
        print(kmeans)
        Hierarchical = AgglomerativeClustering(n_clusters=cluster_n, linkage='ward').fit_predict(sparse_ratings.toarray())
        print(Hierarchical)
        EM = GaussianMixture(n_components=cluster_n, covariance_type="full").fit_predict(sparse_ratings.toarray())
        print(EM)
        clusters = [kmeans,Hierarchical,EM]
        clustersStr = ['kmeans','Hierarchical','EM']
        con = sqlite3.connect("cluster.sqlite3")
        for i in range(0,3):
            clustered = pd.concat([most_rated_movies_1k.reset_index(), pd.DataFrame({'group':clusters[i]})], axis=1)
            clustered = clustered.fillna('')
            clustered.to_sql(clustersStr[i], con, if_exists="replace")
        con.close()
        return Response(status=status.HTTP_200_OK)

    if request.method == 'GET':
        id = request.GET.get('id', None)
        movies = pd.read_csv(
            '../data/movies.dat',
            sep='::', engine='python',
            names=['movieid', 'title', 'genres'],
        )

        ratings = pd.read_csv(
            '../data/ratings.dat',
            sep='::', engine='python',
            names=['userid','movieid','rating','time'],
        )
        #DB에 저장된거로 하자
        ratings_title = pd.merge(ratings, movies[['movieid', 'title']], on='movieid' )

        ##가장 값이 많은 상위 1000개 데이터만 가져온다
        user_movie_ratings =  pd.pivot_table(ratings_title, index='userid', columns= 'title', values='rating')
        most_rated_movies_1k = get_most_rated_movies(user_movie_ratings, 300)

        #이것이 오류 난다면 pandas 업데이트
        sparse_ratings = csr_matrix(pd.SparseDataFrame(most_rated_movies_1k).to_coo())

        # 20 clusters
        predictions = KMeans(n_clusters=20, algorithm='full').fit_predict(sparse_ratings)

        # TODO: Pick a cluster ID from the clusters above
        cluster_number = 7

        # Let's filter to only see the region of the dataset with the most number of values 
        clustered = pd.concat([most_rated_movies_1k.reset_index(), pd.DataFrame({'group':predictions})], axis=1)
        con = sqlite3.connect("cluster.sqlite3")
        clustered = clustered.fillna('')
        print(clustered)
        clustered.to_sql("kmeans", con, if_exists="replace")
        con.close()
        """
        cluster = clustered[clustered.group == cluster_number].drop(['index', 'group'], axis=1)

        cluster = sort_by_rating_density(cluster, n_movies, n_users)
        print(cluster.mean().head(20))
        print()
        print(cluster.fillna(''))
        user_id = 30
        # 유저의 ratings을 다 가져온다.
        user_2_ratings  = cluster.loc[user_id, :]
        print(user_2_ratings)
        # 유저가 보지 않은 영화를 가져온다.
        user_2_unrated_movies =  user_2_ratings[user_2_ratings.isnull()]
        # 그 영화의 다른 유저들의 평균을 가져온다
        avg_ratings = pd.concat([user_2_unrated_movies, cluster.mean()], axis=1, join='inner').loc[:,0]
        # 정렬
        avg_ratings.sort_values(ascending=False)[:20]
        """
        return Response(status=status.HTTP_200_OK)
    

def clustering_errors(k, data):
    kmeans = KMeans(n_clusters=k).fit(data)
    predictions = kmeans.predict(data)
    #cluster_centers = kmeans.cluster_centers_
    # errors = [mean_squared_error(row, cluster_centers[cluster]) for row, cluster in zip(data.values, predictions)]
    # return sum(errors)
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
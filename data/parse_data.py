# -*- coding:utf-8 -*-
import requests
import json
import pandas as pd
import numpy as np
import re

API_URL = 'http://localhost:8000/api/'
headers = {'content-type': 'application/json'}

def create_users(num_users):
    user_data = open('./users.dat', 'r', encoding='ISO-8859-1')
    occupation_map = {
        0: "other", 1: "academic/educator", 2: "artist", 3: "clerical/admin", 4: "college/grad student",
        5: "customer service", 6: "doctor/health care", 7: "executive/managerial", 8: "farmer", 9: "homemaker",
        10: "K-12 student", 11: "lawyer", 12: "programmer", 13: "retired", 14: "sales/marketing",
        15: "scientist", 16:  "self-employed", 17: "technician/engineer", 18: "tradesman/craftsman",
        19: "unemployed", 20: "writer"
    }
    request_data = {'profiles': []}
    for line in user_data.readlines():
        [userid, gender, age, occupation, zipcode] = line.split('::')
        username = 'user' + userid
        age = int(age)
        occupation = occupation_map[int(occupation)]

        request_data['profiles'].append({
            'id': userid,
            'username': username,
            'password': username,
            'age': age,
            'gender': gender,
            'occupation': occupation
        })

        if len(request_data['profiles']) >= num_users:
            break

    response = requests.post(API_URL + 'users/', data=json.dumps(request_data), headers=headers)

def create_movies():
    movie_data = open('./movies.dat', 'r', encoding='ISO-8859-1')
    request_data = {'movies': []}

    ################ 영화 정보 파싱 ################
    metadata = pd.read_csv('./movies_metadata.csv')

    mdata = metadata[['imdb_id', 'poster_path', 'overview', 'production_companies', 'production_countries', 'runtime']]
    links = pd.read_csv("./links.csv")
    links = links[['movieId', 'imdbId']]

    mdata = mdata[~ mdata.imdb_id.isnull()]
    mdata['imdbId'] = mdata.imdb_id.apply(app)
    mdata = mdata[~ mdata.imdbId.isnull()]
    mdata.imdbId = mdata.imdbId.astype(int)

    for idx in range( 4000 ) :
        production_companies = ""
        try :
            production_companies = '|'.join( re.findall( "'name': '(.*?)'", mdata['production_companies'][idx]) )
            mdata['production_companies'][idx] = production_companies

            production_countries = '|'.join( re.findall( "'name': '(.*?)'", mdata['production_countries'][idx]) )
            mdata['production_countries'][idx] = production_countries

            runtime = int( mdata['runtime'][idx] )
            mdata['runtime'][idx] = runtime
        except UnicodeEncodeError :
            continue
        except ValueError :
            mdata['runtime'][idx] = 0

    mdata = mdata[['imdbId', 'poster_path','overview', 'production_companies', 'production_countries', 'runtime']]

    movieinfo = pd.merge(mdata, links, on='imdbId', how='left')
    movieinfo = movieinfo[['movieId', 'poster_path','overview', 'production_companies', 'production_countries', 'runtime']]
    movieinfo = movieinfo.fillna(-1)
    #####################################################


    for line in movie_data.readlines():
        [id, title, genres] = line.split('::')
        genres = genres[:-1].split('|')

        imgpath = ""
        for idx in range( 4000 ) :
            if int(movieinfo['movieId'][idx]) == -1 :
                continue;
            elif int(movieinfo['movieId'][idx]) == int(id) :
                imgpath = "http://image.tmdb.org/t/p/w185" + str(movieinfo['poster_path'][idx])
                overview = movieinfo['overview'][idx]
                production_companies = movieinfo['production_companies'][idx]
                production_countries = movieinfo['production_countries'][idx]
                runtime = movieinfo['runtime'][idx]
                break

        request_data['movies'].append({
            'id': id,
            'title': title,
            'genres': genres,
            'ratings' : 0,
            "viewCnt" :0,
            "imgpath": imgpath,
            "overview": overview,
            "production_companies": production_companies,
            "production_countries": production_countries,
            "runtime": runtime
        })
    response = requests.post(API_URL + 'movies/', data=json.dumps(request_data), headers=headers)


def create_ratings(num_users):
    rating_data = open('./ratings.dat', 'r', encoding='ISO-8859-1')
    request_data = {'ratings': []}
    for line in rating_data.readlines():
        [userid, movieid ,rating, time] = line.split('::')
        if(int(userid) > num_users):
            break
        request_data['ratings'].append({
            'userid': userid,
            'movieid': movieid,
            'rating': rating
        })

    response = requests.post(API_URL + 'ratings/', data=json.dumps(request_data), headers=headers)

def app(x):
    try:
        return int(x[2:])
    except ValueError:
        print(x)

if __name__ == '__main__':
    num_users = 200
    create_movies()
    create_users(num_users)
    create_ratings(num_users)

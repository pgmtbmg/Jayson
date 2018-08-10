# -*- coding:utf-8 -*-
import web
import urllib
import json
import time


movie_ids=[]
for index in range(0,250,50):
    print index
    response=urllib.urlopen('http://api.douban.com/v2/movie/top250?start=%d&count=50' % index)
    data=response.read()
    
    data_json=json.loads(data)
    movie250=data_json['subjects']
    for movie in movie250:
        movie_ids.append(movie['id'])
        print movie['id'],movie['title']
    time.sleep(3)
print movie_ids
print type(movie_ids)


db = web.database(dbn='sqlite', db='MovieSite.db')
def add_movie(data):
    movie=json.loads(data)
    if "title" not in movie:
        print "No exist"
        #db.insert('Not exist',"Don't find it!")
    else:
        print movie['title']
        db.insert('movie',
            id=int(movie['id']),
            title=movie['title'],
            origin=movie['original_title'],
            url=movie['alt'],
            rating=movie['rating']['average'],
            image=movie['images']['large'],
            directors=','.join([d['name'] for d in movie['directors']]),
            casts=','.join([c['name'] for c in movie['casts']]),
            year=movie['year'],
            genres=','.join(movie['genres']),
            countries=','.join(movie['countries']),
            summary=movie['summary'],
    )
count=230
for mid in movie_ids[230:]:
    print count,mid
    response=urllib.urlopen('http://api.douban.com/v2/movie/subject/%s' % mid)
    data=response.read()
    add_movie(data)
    count+=1
    time.sleep(3)

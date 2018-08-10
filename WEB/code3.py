# -*- coding:utf-8 -*-
import web
import time
import urllib
import json

def get_poster(id,url):
    pic=urllib.urlopen(url).read()
    file_name = 'static/%d.jpg' % id
    f=file(file_name,'wb')
    f.write(pic)
    f.close()

db=web.database(dbn='sqlite',db='MovieSite.db')
movies=db.select('movie')
count=0
for movie in movies:
    get_poster(movie.id,movie.image)
    print count,movie.title
    count+=1

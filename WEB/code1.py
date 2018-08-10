# -*- coding:utf-8 -*-
import web
import urllib
import json
import time

db = web.database(dbn='sqlite', db='MovieSite.db')

urls=(
    '/','index',
    '/movie/(\d+)','movie',
    '/cast/(.*)','cast',
)
render=web.template.render('templates/')

class index:
    def POST(self):
        data=web.input()
        condition=r'title like "%' + data.title + r'%"'
        movies=db.select('movie',where=condition)
        count = db.query('SELECT COUNT(*) AS COUNT FROM movie WHERE ' + condition)[0]['COUNT']
        return render.index(movies,count,data.title)
    def GET(self):
        movies=db.select('movie')
        count=248
        return render.index(movies,count,None)
class movie:
    def GET(self,movie_id):
        movie_id=int(movie_id)
        movie=db.select('movie',where='id=$movie_id',vars=locals())[0]
        return render.movie(movie)

class cast:
    def GET(self,cast_name):
        condition=r'casts like"%'+cast_name+r'%"'
        movies=db.select('movie',where=condition)
        count = db.query('SELECT COUNT(*) AS COUNT FROM movie WHERE ' + condition)[0]['COUNT']
        return render.index(movies,count,cast_name)

    
if __name__=="__main__":
    app=web.application(urls,globals())
    app.run()

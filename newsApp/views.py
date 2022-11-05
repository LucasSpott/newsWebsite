from django.shortcuts import render
import requests

def index (request):
    r = requests.get('http://api.mediastack.com/v1/news?access_key=fcdc3acdd0d9b8d6391cca2332ea35b6&countries=jp&limit=8&categories=general')
    res = r.json()
    data = res['data']
    title = []
    description = []
    image = []
    url = []
    for i in data:
     title.append(i['title'])
     description.append(i['description'])
     image.append(i['image'])
     url.append(i['url'])
         
    news = zip(title, description, image, url)
    return render (request, 'newsApp/index.html', {'news':news})
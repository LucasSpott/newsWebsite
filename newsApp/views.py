from django.shortcuts import render
import requests

def index (request):
    r = requests.get('http://api.mediastack.com/v1/news?access_key=e93f64a7b592d333aca8228a62f3c992&countries=jp&limit=8&categories=general')
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
    
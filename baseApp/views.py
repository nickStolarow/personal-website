from django.shortcuts import render, get_object_or_404
import requests
import datetime
import pytz
from .models import Image


def experience(request):
    return render(request, 'baseApp/experience.html', {'experience': 'active'})


def connect(request):
    return render(request, 'baseApp/connect.html', {'connect': 'active'})


def gallery(request):
    image = Image.objects.all()
    return render(request, 'baseApp/gallery.html', {'gallery': 'active', 'image': image})


def photo_of_the_day(request):
    tz = pytz.timezone('America/New_York')
    date = datetime.datetime.now(tz).strftime('%Y-%m-%d')
    url = f'https://api.nasa.gov/planetary/apod?date={date}&hd=True&api_key=wgsgsqhuVb3nULkzTyVNPt0s1pLPwNGOWnTwljml'
    response = requests.get(url)
    potd = response.json()
    return render(request, 'baseApp/photoOfTheDay.html', {'potd': 'active', 'url': potd['url'], 'title': potd['title']})


def about(request):
    return render(request, 'baseApp/about.html', {'about': 'active'})

from django.shortcuts import render
import requests
import datetime


def experience(request):
    return render(request, 'baseApp/experience.html', {'experience': 'active'})


def links(request):
    return render(request, 'baseApp/links.html', {'links': 'active'})


def gallery(request):
    return render(request, 'baseApp/gallery.html', {'gallery': 'active'})


def photo_of_the_day(request):
    date = datetime.datetime.now()
    date = f'{date.year}-{date.month}-{date.day}'
    date = '2021-01-01'
    url = f'https://api.nasa.gov/planetary/apod?date={date}&hd=True&api_key=wgsgsqhuVb3nULkzTyVNPt0s1pLPwNGOWnTwljml'
    response = requests.get(url)
    potd = response.json()
    return render(request, 'baseApp/photoOfTheDay.html', {'potd': 'active', 'url': potd['url'], 'title': potd['title']})


def about(request):
    return render(request, 'baseApp/about.html', {'about': 'active'})


def contact(request):
    return render(request, 'baseApp/contact.html', {'contact': 'active'})

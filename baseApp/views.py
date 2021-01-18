from django.shortcuts import render, get_object_or_404, redirect
import requests
import datetime
import enchant
import random
import time
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
    tz = pytz.timezone('America/Detroit')
    video = False

    if request.GET:
        date = request.GET['date']
    else:
        date = datetime.datetime.now(tz).strftime('%Y-%m-%d')

    url = f'https://api.nasa.gov/planetary/apod?date={date}&hd=True&api_key=wgsgsqhuVb3nULkzTyVNPt0s1pLPwNGOWnTwljml'
    response = requests.get(url)
    potd = response.json()

    if 'msg' in potd:
        return redirect('potd')

    if potd['media_type'] == 'video':
        video = True

    return render(request, 'baseApp/photoOfTheDay.html',
                  {'potd': 'active', 'url': potd['url'], 'title': potd['title'], 'date': date, 'video': video})


def productions(request):
    return render(request, 'baseApp/productions.html', {'productions': 'active'})


def wordscapes(request):
    def solve(letters: list) -> list:
        d = enchant.Dict("en_US")
        length = len(letters)
        known_words = list()
        used_indexes = list()
        timeout = time.time() + 1  # time out after 1 seconds

        while time.time() < timeout:
            word = ''
            used_indexes.clear()
            random_length = random.randrange(3, length + 1, 1)

            for i in range(0, random_length):
                random_index = random.randrange(0, length, 1)

                while random_index in used_indexes:
                    random_index = random.randrange(0, length, 1)

                used_indexes.append(random_index)
                word += letters[random_index]

            if d.check(word) and word not in known_words:
                known_words.append(word)

        return known_words

    def starts_with(words: list, query: str) -> list:
        output = list()
        for word in words:
            if word.startswith(query):
                output.append(word)

        return output

    def ends_with(words: list, query: str) -> list:
        output = list()
        for word in words:
            if word.endswith(query):
                output.append(word)

        return output

    def contains(words: list, query: str) -> list:
        output = list()
        for word in words:
            if query in word:
                output.append(word)

        return output

    def length_of(words: list, query: int) -> list:
        output = list()
        for word in words:
            if len(word) == query:
                output.append(word)

        return output

    letters = ''
    letters_og = ''
    starts_query = ''
    ends_query = ''
    contains_query = ''
    starts_words = ''
    ends_words = ''
    contains_words = ''
    length_words = ''
    length = ''

    if request.GET:
        letters_og = request.GET['letters'].lower()
        letters = letters_og.replace(' ', '').split(',')
        starts_query = request.GET['starts'].lower()
        ends_query = request.GET['ends'].lower()
        contains_query = request.GET['contains'].lower()
        if request.GET['length'] != '':
            length = int(request.GET['length'])

        words = solve(letters)
        if len(letters) != 0:
            starts_words = starts_with(words, starts_query)
            ends_words = ends_with(words, ends_query)
            contains_words = contains(words, contains_query)
            if length != '':
                length_words = length_of(words, length)

    if length != '':
        result = set(starts_words).intersection(ends_words).intersection(contains_words).intersection(length_words)
    else:
        result = set(starts_words).intersection(ends_words).intersection(contains_words)

    return render(request, 'baseApp/wordscapes.html',
                  {'productions': 'active', 'letters': letters_og, 'starts': starts_query, 'ends': ends_query,
                   'contains': contains_query, 'length': length, 'result': result})


def about(request):
    return render(request, 'baseApp/about.html', {'about': 'active'})

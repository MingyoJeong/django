from django.shortcuts import render
from datetime import datetime
import requests
import os


# Create your views here.
def index(request):
    return render(request, 'books/index.html')

def graduation(request):
    time1 = datetime(2019, 6, 27)
    time2 = datetime.now()
    result = time1 - time2
    context = {
        'result': result,
        'time1': time1,
        'time2': time2,
    }
    return render(request, 'books/graduation.html', context)

def imagepick(request):
    return render(request, 'books/imagepick.html')

def today(request):
    key = '5978b13f0e54f913a1c9c97575f29e02'
    url = 'https://api.openweathermap.org/data/2.5/weather?q=Seoul,kr&lang=kr&APPID=' + key
    data = requests.get(url).json()
    weather = {
        'status': data['weather'][0]['description'],
        'temp': round(data['main']['temp']-273.15, 1),
        'temp_min': data['main']['temp_min']-273.15,
        'temp_max': data['main']['temp_max']-273.15,
    }
    print(type(weather['temp']))
    context = {
        'weather': weather
    }
    return render(request, 'books/today.html', context)

def ascii_new(request):
    fonts = [
        'short', 'utopia', 'rounded', 'acrobatic', 'alligator'
    ]
    context = {
        'fonts': fonts,
    }
    return render(request, 'books/ascii_new.html', context)

def ascii_make(request):
    text = request.GET.get('text')
    font = request.GET.get('font')
    url = f'http://artii.herokuapp.com/make?text={text}&font={font}'
    result = requests.get(url).text
    context = {
        'result': result,
    }
    return render(request, 'books/ascii_make.html', context)

def original(request):
    return render(request, 'books/original.html')

def translated(request):
    korean = request.GET.get('text')
    naver_client_id = os.getenv("NAVER_CLIENT_ID")
    naver_client_secret = os.getenv("NAVER_CLIENT_SECRET")

    papago_url = "https://openapi.naver.com/v1/papago/n2mt"

    # 네이버에 Post 요청을 위해서 필요한 내용들
    headers = {
        "X-Naver-Client-Id": naver_client_id,
        "X-Naver-Client-Secret": naver_client_secret
    }

    data = {
        "source": "ko",
        "target": "en",
        "text": korean
    }

    papago_response = requests.post(papago_url, headers=headers, data=data).json()
    english = papago_response["message"]["result"]["translatedText"]

    context = {
        'korean': korean,
        'english': english,
    }
    return render(request, 'books/translated.html', context)

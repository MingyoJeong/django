from django.shortcuts import render
import random
from datetime import datetime
import request
import requests

# Create your views here.
def index(request):
    # print(request)
    # print(type(request))
    print(request.META)
    return render(request, 'index.html')


def dinner(request):
    menus = ['족발', '햄버거', '치킨', '초밥']
    pick = random.choice(menus)
    context = {'pick' : pick}
    return render(request, 'dinner.html', context)


def hello(request, name):
    context = {'name': name,}
    return render(request, 'hello.html', context)

# 자기소개 / 이름과 나이를 url 로 받아서 출력
def introduce(request, name, age):
    context = {
        'name' : name,
        'age' : age,
    }
    return render(request, 'introduce.html', context)


# 숫자 2개를 variable routing 으로 받아 곱셈 결과를 출력
def times(request, num1, num2):
    result = num1 * num2
    context = {
        'num1': num1,
        'num2': num2,
        'result' : result,
    }
    return render(request, 'time.html', context)
# 원의 반지름 값음 variable routing 으로 받아 원의 넓이를 출력
def area():
    area = (r ** 2) * 3.14
    context = {
        'r' : r,
        'area.html' : area,
    }
    return render(request, 'area.html', context)


def dtl_example(request):
    menus = ['짜장면', '탕수육', '짬뽕', '양장피']
    my_sentence = 'Life is short, You need python'
    messages = ['apple', 'banana', 'cucumber', 'mango']
    datetimenow = datetime.now()
    empty_list = []
    context = {
        'menus': menus,
        'my_sentence': my_sentence,
        'messages': messages,
        'datetimenow': datetimenow,
        'empty_list': empty_list,
    }
    return render(request, 'dtl_example.html', context)


def throw(request):
    return render(request, 'throw.html')

def catch(request):
    # print(request.GET)
    message = request.GET.get('message')
    context = {'message': message,}
    return render(request, 'catch.html', context)

def artii(request):
    return render(request, 'artii.html')

def result(request):
    # 1. form 에서 날아온 데이터를 받는다.
    word = request.GET.get('word')
    # 2. artii api(http://artii.herokuapp.com/fonts_list) 로 요청을 보내 응답 결과를 text 로 저장한다.
    fonts = requests.get('http://artii.herokuapp.com/fonts_list').text
    # 3. 저장한 데이터를 list 로 바꾼다.
    fonts_list = fonts.split('\n')
    print(fonts_list)
    # 4. list 안에 들어있는 요소(font) 하나를 선택해서 저장한다.
    font = random.choice(fonts_list)
    # 5. 우리가 전달한 데이터와 list 안에 font 를 가지고 다시 요청을 보내 해당 응답
    # 결과를 저장한다. (.text)
    result = requests.get(f'http://artii.herokuapp.com/make?text={word}&font={font}').text
    # 6. 최종적으로 저장한 데이터를 template 으로 넘겨준다.
    context = {'result': result,}
    print(result)
    return render(request, 'result.html', context)

def user_new(request):
    return render(request, 'user_new.html')

def user_create(request):
    name = request.POST.get('name')
    pwd = request.POST.get('pwd')
    context = {
        'name': name,
        'pwd': pwd,
    }
    return render(request, 'user_create.html', context)

def static_example(request):
    return render(request, 'static_example.html')


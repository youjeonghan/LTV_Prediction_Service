from django.shortcuts import render
from django.http import HttpResponse


def index(requset):
    return HttpResponse("안녕하세요 LTV 예측 서비스 입니다.")

from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(resquest, nome, idade):
    return HttpResponse('<h1>Hellow {} de {} anos</h1>'.format(nome, idade))
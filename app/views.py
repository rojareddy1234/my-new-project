from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(request):
    return HttpResponse ('hai this is my first views page')
def second(request):
    return HttpResponse('<h1>this is my second response<h1>')
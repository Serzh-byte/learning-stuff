from django.shortcuts import render
import requests


def home(request):
    return render(request, 'something/home.html')

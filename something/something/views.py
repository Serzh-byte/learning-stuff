from django.shortcuts import render
import requests


def simple(request):
    return render(request, 'something/simple.html')

def forms(request):
    return render(request, 'something/forms.html')
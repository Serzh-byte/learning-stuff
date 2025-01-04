from django.shortcuts import render
import requests


def simple(request):
    return render(request, 'something/simple.html')

def forms(request):
    return render(request, 'something/forms.html')

def home(request):
    if request.method == 'POST':
        return render(request, 'something/home.html')
    return render(request, 'something/home.html')

def name(request):
    if request.method == 'POST':
        name = request.POST.get('name')  # Get the name from the form data
        return render(request, 'something/name.html', {'name': name})
    return render(request, 'something/name.html',)  # Handle GET request (if needed)

def bt1(request):
    if request.method == 'POST':
        return render(request, 'something/bt1.html')
    return render(request, 'something/bt1.html')
    
def bt2(request):
    if request.method == 'POST':
        return render(request, 'something/bt2.html')
    return render(request, 'something/bt2.html')


from django.shortcuts import render


def hello(request):
    if request.method == 'POST':
        return render(request, 'jv/hello.html')
    return render(request, 'jv/hello.html')

def counter(request):
    if request.method == 'POST':
        return render(request, 'jv/counter.html')
    return render(request, 'jv/counter.html')

def colors(request):
    if request.method == 'POST':
        return render(request, 'jv/colors.html')
    return render(request, 'jv/colors.html')
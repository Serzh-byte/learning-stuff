from django.shortcuts import render


def hello(request):
    if request.method == 'POST':
        return render(request, 'jv/hello.html')
    return render(request, 'jv/hello.html')

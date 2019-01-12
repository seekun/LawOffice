from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'init/index.html')

def services(request):
    return render(request, 'init/services.html')


def test1(request):
    return render(request, 'init/test1.html')
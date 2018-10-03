from django.shortcuts import render


def index(request):
    return render(request, 'home/index.html')

def logIn(request):
    return render(request, 'login.html')

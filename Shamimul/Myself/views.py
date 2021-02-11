from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def edu(request):
    return render(request, 'education.html')


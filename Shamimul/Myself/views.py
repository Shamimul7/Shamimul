from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def edu(request):
    return render(request, 'education.html')


def gallery(request):
    return render(request, 'gallery.html')


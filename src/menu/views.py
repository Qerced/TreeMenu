from django.shortcuts import render


def index(request, slug):
    return render(request, 'menu/home.html', {'slug': slug})

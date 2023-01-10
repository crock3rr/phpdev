from django.shortcuts import render

from app.models import MainPage


def main_page(request):
    data = {
        'profession': MainPage.objects.get(id=1)
    }
    return render(request, "main.html", context=data)


def hh_page(request):
    return render(request, "hh.html")

import pandas as pd
import requests as req

from django.shortcuts import render
from app.models import *


def main_page(request):
    data = {
        'title': MainPage.objects.get(id=1).title,
        'description': MainPage.objects.get(id=1).description.split('\r\n')
    }
    return render(request, "main.html", context=data)


def hh_page(request):
    date = Vacancies.objects.get(id=1).date
    result = Vacancies.get_result_from_api(date)
    return render(request, "hh.html", context={'table': result.to_html(index=False)})


def relevance_page(request):
    return render(request, "relevance.html")

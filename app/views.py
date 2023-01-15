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
    data = {
        'salary': pd.read_csv(Relevance.objects.get(title='Зарплаты').content).to_html(index=False),
        'vacancy': pd.read_csv(Relevance.objects.get(title='Вакансии').content).to_html(index=False),
        'salary_php': pd.read_csv(Relevance.objects.get(title='Зарплаты php').content).to_html(index=False),
        'vacancy_php': pd.read_csv(Relevance.objects.get(title='Вакансии php').content).to_html(index=False)
    }
    return render(request, "relevance.html", context=data)

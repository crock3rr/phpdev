import pandas as pd
import requests as req

from django.shortcuts import render
from app.models import MainPage


def main_page(request):
    data = {
        'profession': MainPage.objects.get(id=1)
    }
    return render(request, "main.html", context=data)


def hh_page(request):
    result = []
    date = '15.12.2022'
    for page in range(20):
        path = f'https://api.hh.ru/vacancies?specialization=1&date_from={date}&date_to={date}&page={page}&per_page=100'
        res = req.get(path).json()
        [result.append([el['name'], el['snippet']['responsibility'], el['snippet']['requirement'],
                        el['employer']['name'], el['salary']['from'] if el['salary'] is not None else None,
                        el['salary']['to'] if el['salary'] is not None else None,
                        el['salary']['currency'] if el['salary'] is not None else None, el['area']['name'],
                        el['published_at']]) for el in res['items']]

    frame = pd.DataFrame(result, columns=["name", "description", "key_skills", "employer_name", "salary_from",
                                          "salary_to", "salary_currency", "area_name", "published_at"]).fillna("")
    frame = frame[frame.name.str.contains("php") | frame.name.str.contains("пхп") |
                  frame.name.str.contains("рнр")].sort_values('published_at')[:10]
    result = {
        'table': frame.to_html(index=False)
    }
    return render(request, "hh.html", context=result)

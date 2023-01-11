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
    vacancies = []
    date = Vacancies.objects.get(id=1).date
    for index in range(20):
        path = f'https://api.hh.ru/vacancies?specialization=1&date_from={date}&date_to={date}&page={index}&per_page=100'
        res = req.get(path).json()
        for vacancy in res['items']:
            salary = None
            if vacancy['salary'] is not None:
                general = list(filter(None, [vacancy["salary"]["from"], vacancy["salary"]["to"]]))
                salary = f'{"-".join(list(map(str, general)))} {vacancy["salary"]["currency"]}'
            vacancies.append([vacancy['name'], vacancy['snippet']['responsibility'], vacancy['snippet']['requirement'],
                              vacancy['employer']['name'], salary, vacancy['area']['name'], vacancy['published_at']])

    df = pd.DataFrame(vacancies, columns=["Название вакансии", "Описание вакансии", "Навыки", "Компания", "Оклад",
                                          "Название региона", "Дата публикации вакансии"]).fillna("")
    df = df[df['Название вакансии'].str.lower().str.contains("php") |
            df['Название вакансии'].str.lower().str.contains("пхп") |
            df['Название вакансии'].str.lower().str.contains("рнр")].sort_values('Дата публикации вакансии')[:10]
    data = {
        'table': df.to_html(index=False)
    }
    return render(request, "hh.html", context=data)

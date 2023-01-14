import datetime

import pandas as pd
import requests as req
from django.db import models


class MainPage(models.Model):
    title = models.CharField('Название профессии', max_length=70)
    description = models.TextField('Описание профессии')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"


class Vacancies(models.Model):
    date = models.CharField('Дата публикации вакансии', max_length=20)

    def __str__(self):
        return 'Дата'

    @staticmethod
    def get_result_from_api(date):
        vacancies = []
        for index in range(20):
            path = f'https://api.hh.ru/vacancies?specialization=1&date_from={date}&date_to={date}&page={index}&per_page=100'
            res = req.get(path).json()
            for vacancy in res['items']:
                salary = None
                if vacancy['salary'] is not None:
                    general = list(filter(None, [vacancy["salary"]["from"], vacancy["salary"]["to"]]))
                    salary = f'{"-".join(list(map(str, general)))} {vacancy["salary"]["currency"]}'
                vacancies.append(
                    [vacancy['name'], vacancy['snippet']['responsibility'], vacancy['snippet']['requirement'],
                     vacancy['employer']['name'], salary, vacancy['area']['name'], vacancy['published_at']])

        df = pd.DataFrame(vacancies, columns=["Название вакансии", "Описание вакансии", "Навыки", "Компания", "Оклад",
                                              "Название региона", "Дата публикации вакансии"]).fillna("")
        df = df[df['Название вакансии'].str.lower().str.contains("php") |
                df['Название вакансии'].str.lower().str.contains("пхп") |
                df['Название вакансии'].str.lower().str.contains("рнр")].sort_values('Дата публикации вакансии')[:10]
        df['Дата публикации вакансии'] = df['Дата публикации вакансии'].apply(
            lambda x: f'{datetime.datetime.strptime(x, "%Y-%m-%dT%H:%M:%S+%f").day}'
                      f'.{datetime.datetime.strptime(x, "%Y-%m-%dT%H:%M:%S+%f").month}'
                      f'.{datetime.datetime.strptime(x, "%Y-%m-%dT%H:%M:%S+%f").year}')
        return df

    class Meta:
        verbose_name = "Дата"
        verbose_name_plural = "Последние вакансии"

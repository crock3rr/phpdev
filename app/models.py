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

    class Meta:
        verbose_name = "Дата"
        verbose_name_plural = "Последние вакансии"

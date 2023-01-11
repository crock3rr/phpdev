# Generated by Django 4.1.5 on 2023-01-11 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=20, verbose_name='Дата публикации вакансии')),
            ],
            options={
                'verbose_name': 'Дата',
                'verbose_name_plural': 'Последние вакансии',
            },
        ),
    ]
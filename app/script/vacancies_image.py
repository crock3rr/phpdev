import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


def create_image(csv_name, column_info, title_image):
    fig, ax = plt.subplots()
    x = pd.read_csv(f'../csv/{csv_name}.csv')['Год'].tolist()
    ax.bar(np.arange(len(x)), pd.read_csv(f'../csv/{csv_name}.csv')[column_info].tolist())
    ax.tick_params(axis='x', rotation=90)
    ax.tick_params(axis='y')
    ax.set_xticks(np.arange(len(x)), x)
    ax.set_title(title_image)
    ax.grid(axis='y')
    plt.tight_layout()
    plt.savefig(f'../static/vacancies/{csv_name}.png')


create_image('salary', 'Уровень зарплат', 'Динамика уровня зарплат по годам')
create_image('vacancy', 'Количество вакансий', 'Динамика количества вакансий по годам')
create_image('salary_php', 'Уровень зарплат php', 'Динамика уровня зарплат по годам для php-программистов')
create_image('vacancy_php', 'Количество вакансий php', 'Динамика количества вакансий по годам для php-программистов')

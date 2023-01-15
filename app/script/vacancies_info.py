import pandas as pd


def generate_average(record):
    currencies = {"": 1, "AZN": 35.68, "BYR": 23.91, "EUR": 59.90, "GEL": 21.74, "KGS": 0.76, "KZT": 0.13, "RUR": 1,
                  "UAH": 1.64, "USD": 60.66, "UZS": 0.0055}
    average = list(map(float, list(filter(None, [record.salary_from, record.salary_to]))))
    return float(sum(average) / len(average) * currencies[record.salary_currency]) if len(average) > 0 else None


df = pd.read_csv("../csv/vacancies_with_skills.csv", low_memory=False).fillna("")
df.insert(2, 'avg_salary', df.apply(lambda x: generate_average(x), axis=1))
df = df.drop(columns=['salary_from', 'salary_to', 'salary_currency'])
df.published_at = df.published_at.apply(lambda x: x[:4])
df_profession = df[df.name.str.lower().str.contains("php") | df.name.str.lower().str.contains("пхп") |
                   df.name.str.lower().str.contains("рнр")]

salary = df.groupby('published_at')['avg_salary'].mean().apply(lambda x: int(x))
vacancy = df.groupby('published_at')['published_at'].count()
salary_php = df_profession.groupby('published_at')['avg_salary'].mean().apply(lambda x: int(x))
vacancy_php = df_profession.groupby('published_at')['published_at'].count()

pd.DataFrame({'Год': salary.index.tolist(), 'Уровень зарплат': salary.tolist()}).to_csv(
    "../csv/salary.csv", index=False)
pd.DataFrame({'Год': vacancy.index.tolist(), 'Количество вакансий': vacancy.tolist()}).to_csv(
    "../csv/vacancy.csv", index=False)
pd.DataFrame({'Год': salary_php.index.tolist(), 'Уровень зарплат php': salary_php.tolist()}).to_csv(
    "../csv/salary_php.csv", index=False)
pd.DataFrame({'Год': vacancy_php.index.tolist(), 'Количество вакансий php': vacancy_php.tolist()}).to_csv(
    "../csv/vacancy_php.csv", index=False)


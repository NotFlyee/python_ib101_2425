import datetime
from math import sin, pi


def convert_date(date: str) -> datetime:
    day, month, year = map(int, date.split('.'))
    return datetime.datetime(day=day, month=month, year=year)


def get_biorhythm_value(birth_date: datetime, biorhythm_date: datetime, body: str) -> float:
    T = biorhythm_date - birth_date
    P = {
        'sun': datetime.timedelta(days=33),
        'moon': datetime.timedelta(days=28),
        'earth': datetime.timedelta(days=23)
    }
    return round(sin((2 * pi * T / P[body])) * 100, 2)

birth_date = convert_date(input())
biorhythm_date = convert_date(input())

print(get_biorhythm_value(birth_date, biorhythm_date, 'earth'))
print(get_biorhythm_value(birth_date, biorhythm_date, 'moon'))
print(get_biorhythm_value(birth_date, biorhythm_date, 'sun'))

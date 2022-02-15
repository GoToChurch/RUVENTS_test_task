import pandas as pd
from pandas.tseries.offsets import LastWeekOfMonth

test_data = pd.read_csv('Tasks.csv')
test_data = test_data.drop(0)

def num1():
    '''Задание: Сколько четных чисел в этом столбце?'''

    test_data_num1 = test_data[['num1']].astype(int) # Преобразуем данные в столбце в int
    return len(test_data_num1.query('num1 % 2 == 0'))

def num2():
    '''Задание: Сколько простых чисел в этом столбце?'''

    def is_prime(n):
        '''Функция для проверки числа на простоту'''
        if n % 2 == 0:
            return n == 2
        d = 3
        while d * d <= n and n % d != 0:
            d += 2
        return d * d > n

    test_data_num2 = pd.to_numeric(test_data['num2'])
    primes = []

    for i in test_data_num2:
        if is_prime(i):
            primes.append(i)

    return len(primes)

def num3():
    '''Задание: Сколько чисел, меньших 0.5 в этом столбце?'''

    test_data_num3 = test_data['num3']
    answer = []

    for i in test_data_num3:
        i = i.replace(' ', '').replace(',', '.') # Преобразуем дынные к одному виду
        if not i.startswith('0'): # Добавляем ноль в начало строки, если он отсутствует
            i = i[::-1] + '0'
            i = i[::-1]
        if float(i) < 0.5:
            answer.append(i)

    return len(answer)

def date1():
    '''Задание: Столько вторников в этом столбце?'''

    test_data_date1 = test_data['date1']
    tuesdays = []

    for i in test_data_date1:
        if i.startswith('Tue'):
            tuesdays.append(i)

    return len(tuesdays)

def date2():
    '''Задание: Столько вторников в этом столбце?'''

    test_data_date2 = pd.to_datetime(test_data.date2) # Преобразуем данные в формат date
    tuesdays = []

    for i in test_data_date2:
        if i.strftime('%a') == 'Tue':
            tuesdays.append(i)

    return len(tuesdays)

def date3():
    '''Задание: Сколько последних вторников месяца в этом столбце?'''

    test_data_date3 = pd.to_datetime(test_data.date3)
    last_tuesdays = []

    def last_tues(year):
        '''Функция, которая выводит все последние вторники в необходимом году'''

        return list((pd.date_range('1/1/' + str(year), periods=12, freq='M')
                - LastWeekOfMonth(n=1, weekday=1)).strftime('%m-%d-%Y'))

    for i in test_data_date3:
        if i in last_tues(i.year):
            last_tuesdays.append(i)

    return len(last_tuesdays)

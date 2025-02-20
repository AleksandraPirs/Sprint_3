from random import randint

class Person:
    user_name = 'Саша'
    email = f'guseva_15@gmail.com'
    password = f'200196'

class RandomData:
    user_name = 'Тест'
    email = f'test{randint(0, 999)}@gmail.com'
    password = f'{randint(1000, 9999)}Qwe'
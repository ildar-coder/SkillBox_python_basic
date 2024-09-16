# TODO здесь писать код
import random


class KillError(Exception):
    def __str__(self):
        return 'Произошла ошибка {}'.format(self.__class__.__name__)


class DrunkError(Exception):
    def __str__(self):
        return 'Произошла ошибка {}'.format(self.__class__.__name__)


class CarCrashError(Exception):
    def __str__(self):
        return 'Произошла ошибка {}'.format(self.__class__.__name__)


class GluttonyError(Exception):
    def __str__(self):
        return 'Произошла ошибка {}'.format(self.__class__.__name__)


class DepressionError(Exception):
    def __str__(self):
        return 'Произошла ошибка {}'.format(self.__class__.__name__)


def one_day():
    errors = (KillError, DrunkError, CarCrashError, GluttonyError, DepressionError)
    karma_value = random.randint(1, 7)
    rand_num = random.randint(1, 10)
    rand_error = random.randint(0, 4)
    if rand_num == 1:
        raise errors[rand_error]
    else:
        return karma_value


KARMA_TARGET = 500
with open('karma.log', 'w', encoding='UTF-8') as file:
    karma = 0
    while True:
        try:
            karma += one_day()
        except (KillError, DrunkError, CarCrashError, GluttonyError, DepressionError) as e:
            print(f'{e}!')
            file.write('Произошла ошибка {}\n'.format(e))
        if karma >= KARMA_TARGET:
            break

print(f'Цель достигнута! Карма: {karma}')

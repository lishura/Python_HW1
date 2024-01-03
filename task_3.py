# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать “больше” или “меньше” после каждой попытки.
# Для генерации случайного числа используйте код:
# from random import randintnum = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
rand_num = randint(LOWER_LIMIT, UPPER_LIMIT)

attempt = 10

for _ in range (0, attempt):
    num = int(input(f'Угадайте целое число от {LOWER_LIMIT} до {UPPER_LIMIT}. Осталось {attempt} попыток. Введите число: '))
    if num == rand_num:
        print(f'Ура! Вы угадали! Загаданное число {rand_num}')
        break
    elif num < rand_num:
        print('Не угадали. Загаданное число больше.')
        attempt -= 1
    else:
        print('Не угадали. Загаданное число меньше.')
        attempt -= 1
        if attempt == 0:
            print('Сожалеем. Количество попыток истекло.')
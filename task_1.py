# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника.
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других,
# то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.


from random import uniform

a = round(uniform(0, 1000), 2)
b = round(uniform(0, 1000), 2)
c = round(uniform(0, 1000), 2)

print (f'Проверяем треугольник со сторонами {a=}, {b=}, {c=}.')

if a < (b + c) and b < (a + c) and c < (a + b):
    print('Такой треугольник существует.')
    if a == b == c:
        print('И он является равносторонним.')
    elif a == b or a == c or b == c:
        print('И он является равнобедренным.')
    else:
        print('И он является разносторонним.')
else:
    print('Такой треугольник не существует.')







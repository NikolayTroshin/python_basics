"""
4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо
выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень!
ВНИМАНИЕ: использование встроенной функции = задание не принято
Постараться придумать свой алгоритм без **
"""


def my_func(a, b):      # возведение в любую целую степень
    i = 1
    a1 = a
    while i < abs(b):
        a1 = a1 * a
        i += 1
    if b > 0:           # если степень положительная
        return a1
    elif b < 0:         # если степень отрицательная
        return 1 / a1
    return 1


x = 4
y = -3
print('вычисление через my_func ', my_func(x, y))
print('вычисление через ** для проверки ', x ** y)

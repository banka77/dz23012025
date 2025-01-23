def nod(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


def nok(a, b):
    return (a * b) // nod(a, b)


def nok_three(a, b, c):
    return nok(nok(a, b), c)


A = int(input("Введите первое натуральное число: "))
B = int(input("Введите второе натуральное число: "))
C = int(input("Введите третье натуральное число: "))

if A <= 0 or B <= 0 or C <= 0:
    print('Ошибка!')
else:
    NOK = nok_three(A, B, C)
    print(f'Наименьшее общее кратное {A},{B} и {C}: {NOK}')
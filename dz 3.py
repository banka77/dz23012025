def nod(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


def nod_of_four_numbers(A, B, C, D):
    return nod(nod(A, B), nod(C, D))


A = int(input("Введите первое натуральное число: "))
B = int(input("Введите второе натуральное число: "))
C = int(input("Введите третье натуральное число: "))
D = int(input("Введите четвертое натуральное число:"))
if A <= 0 or B <= 0 or C <= 0 or D <= 0:
    print('Ошибка!')
else:
    NOD = nod_of_four_numbers(A, B, C, D)
    print(f"Наибольший общий делитель чисел {A}, {B}, {C} и {D} : {NOD}")
def nod (a,b):
    while a != b :
        if a > b:
            a -= b
        else:
            b -= a
    return a

def nok (a,b):
    return (a*b) // nod(a,b)

A = int(input('Введите 1 натуральное число:'))
B = int(input('Введите 2 натуральное число:'))

if A <= 0 or B <= 0:
    print('Ошибка!')
else:
    NOD = nod(A,B)
    NOK = nok(A,B)
    print(f'Наибольший общий делитель {A} и {B}: {NOD}')
    print(f'Наименьшее общее кратное {A} и {B}: {NOK}')

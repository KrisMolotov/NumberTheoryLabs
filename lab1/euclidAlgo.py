print('Введите число a: ')
a = int(input())
print('Введите число b: ')
b = int(input())

a1, b1 = a, b
while a1 != b1:
    if a1 > b1:
        a1 = a1 - b1
    else:
        b1 = b1 - a1

print('НОД =', a1)
print('НОК =', a * b // a1)

n = int(input('Введите номер билета: '))

b1 = n // 1000
a1 = b1 % 10
b11 = b1 // 10
d1 = b11 % 10
c1 = b11 // 10
result1 = a1 + d1 + c1 

b2 = n % 1000
a2 = b2 % 10
b22 = b2 // 10
d2 = b22 % 10
c2 = b22 // 10
result2 = a2 + d2 + c2 

if result1 == result2:
    print(f'Билет под номером {n} счастливый')
else:
    print(f'Билет под номером {n} обычный')
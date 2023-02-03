n = int(input('Введите 3 значное число: '))

a = n % 10
n = n // 10
b = n % 10
c = n // 10

print(a + b + c)
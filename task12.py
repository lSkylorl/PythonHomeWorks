s = int(input('Введите сумму числа: '))
p = int(input('Введите произведение числа: '))
res = 0

for i in range(s + p):
    if res == 1:
        break
    for j in range(s + p):
        if i + j == s and i * j == p:
            res = 1 
            print(i, j)


from random import randint

n = int(input('Введите кол-во элементов массива: '))
listRand = [randint(1, 9) for i in range(n)]
print(listRand)

numX = int(input('Введите число: '))

for i in listRand:
    v = 0
    for j in listRand:
        if i == j:
            v += 1 
print(f"Число {numX} повторяется {v} раз/а")
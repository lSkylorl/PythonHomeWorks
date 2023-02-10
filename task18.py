from random import randint

n = int(input('Введите кол-во элементов массива: '))
listRand = [randint(1, 9) for i in range(n)]
print(listRand)

numX = int(input('Введите число: '))
res = listRand[0]

for i in listRand:
    if abs(i - numX) < abs(res - numX):
        res = i
print(f"Ближайшее число к числу {numX} - {res}")
a1 = int(input("Введите первый элемент: "))
d = int(input("Введите шаг прогрессии: "))
n = int(input("Введите кол-во элементов: "))

progr = [a1 + (i - 1) * d for i in range(1, n + 1)]

print(*progr)
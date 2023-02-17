def expon(a, b):
    if b == 0:
        return 1
    if b % 2 == 0:
        return expon(a, b // 2) * expon(a, b // 2)
    else: 
        return expon(a, b - 1) * a

a = int(input("Введите число a: "))
b = int(input("Введите число b: "))

print(expon(a, b))
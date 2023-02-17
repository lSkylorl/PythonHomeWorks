def rSum(a, b):
    a += 1
    b -= 1
    if b > 0:
        return rSum(a, b)
    else:
        return a
    
a = int(input("Введите число a: "))
b = int(input("Введите число b: "))

print(rSum(a, b))
n = int(input('Введите кол-во долек по горизонтали: '))
m = int(input('Введите кол-во долек по вертикали: '))
k = int(input('Сколько долек отломить: '))

if k < n * m and ((k % n == 0) or (k % m == 0)):
    print('получится')
else:
    print('не получится')
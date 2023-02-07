from random import randint

quantity = int(input('Кол-во монет: '))
coins = [randint(0, 1) for i in range(quantity)]
print(f'монеты на столе: {coins}')
i = 0
ans1 = 0
ans2 = 0

while i <= quantity-1:
    if coins[i] == 1:
        ans1 += 1
    else:
        ans2 += 1
    i +=1   

if ans1 > ans2:
    print(f'кол-во операций чтобы монетки были одинаковой стороной : {ans2}')
else:
    print(f'кол-во операций чтобы монетки были одинаковой стороной : {ans1}')
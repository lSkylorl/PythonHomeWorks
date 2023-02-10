inpTxt = input(("Введите слово: "))

EngLibrary = {
    1:'aeioulnstr',
    2: 'dg',
    3: 'bcmp',
    4:'fhvwy',
  	5:'k',
  	8:'jx',
  	10:'qz'
}
RusLibrary = {
    1:'авеинорст',
    2:'дклмпу',
  	3:'бгёья',
  	4:'йы',
  	5:'жзхцч',
  	8:'шэю',
  	10:'фщъ'
}

rusSum = sum(
    j for i in inpTxt for j, 
    f in RusLibrary.items() if i in f
    )

EngSum = sum(
    j for i in inpTxt for j, 
    f in EngLibrary.items() if i in f
    )

if rusSum > EngSum:
    print(rusSum)
else:
    print(EngSum)
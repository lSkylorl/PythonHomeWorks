import random


# Императивный стиль
def sort_list_imperative(number):
    if len(number) <= 1:
        return number
    else:
        q = random.choice(number)
        Snums = []
        Mnums = []
        Enums = []
        for n in number:
            if n < q:
                Snums.append(n)
            elif n > q:
                Mnums.append(n)
            else:
                Enums.append(n)
        return sort_list_imperative(Snums) + Enums + sort_list_imperative(Mnums)



# Декларативный стиль
def sort_list_declarative(number):
    print(sorted(number, reverse=True))



if __name__ == '__main__':
    numbers = [1, 4, 6, -7, 10, 0, 4, 6, 3]
    lst = sort_list_imperative(numbers)
    lst1 = lst[::-1]
    print(lst1)
    sort_list_declarative(numbers)
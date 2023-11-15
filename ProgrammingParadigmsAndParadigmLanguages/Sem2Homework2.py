
# В примере выбрана процедурная парадигма так как она основана на вызове процедур и пошагово их выполняя
# что способствует простому решению данной задачи.

def multiplication_table(n):
    for i in range(1, n + 1):
        for j in range(1, 10):
            print(f"{i} * {j} = {i * j}")
        print('')

def main():
    n = int(input("Введите число n: "))
    multiplication_table(n)

if __name__ == "__main__":
    main()
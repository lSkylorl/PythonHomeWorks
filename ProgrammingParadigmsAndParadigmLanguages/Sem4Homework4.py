import math


def pearson_correlation(array1, array2):
    # Проверка на длину массивов
    if len(array1) != len(array2):
        raise ValueError("Массивы должны быть одинаковой длины!")

    n = len(array1)

    mean_x = sum(array1) / n
    mean_y = sum(array2) / n

    variance_x = sum([(xi - mean_x) ** 2 for xi in array1]) / float(len(array1))
    variance_y = sum([(yi - mean_y) ** 2 for yi in array2]) / float(len(array2))

    covariance = sum([(xi - mean_x) * (yi - mean_y) for xi, yi in zip(array1, array2)]) / float(len(array1))
    correlationPirs = covariance / (math.sqrt(variance_x * variance_y))

    return correlationPirs


array1 = [11, 52, 13, 14, 32, 30, 16, 21]
array2 = [19, 20, 13, 19, 31, 26, 17, 10]

correlationPirs = round(pearson_correlation(array1, array2), 3)
print(f"Корреляция Пирсона: {correlationPirs}")
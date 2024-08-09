# Домашняя работа по уроку "Функции в Python.Функция с параметром"

def get_matrix(n, m, value): # создание функции get_matrix
    matrix = [] # создание пустого списка матрицы
    for i in range(n):  # цикл создания n-строк матрицы
        row = []    # создание пустого списка строк
        for j in range(m):  # цикл создания m-столбцов матрицы
            row.append(value)   # присвоение значений value элементам строк
        matrix.append(row)  # присвоение значений row столбцам матрицы
    return matrix   # возвращение функцией get_matrix сформированной матрицы matrix
result1 = get_matrix(2, 2, 10)  # вводные данные для матрицы result1
result2 = get_matrix(3 ,5 ,42)  # вводные данные для матрицы result2
result3 = get_matrix(4, 2,13)   # вводные данные для матрицы result3
print(result1) # вывод на консоль матрицы result1
print(result2) # вывод на консоль матрицы result2
print(result3) # вывод на консоль матрицы result3
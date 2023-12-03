def calculate_row_sum(matrix):
    # Функция calculate_row_sum принимает матрицу matrix и возвращает список S, где каждый элемент равен сумме элементов в соответствующей строке

    # Создаем пустой список S
    s = []

    # Проходим по каждой строке в матрице
    for row in matrix:
        # Считаем сумму элементов в строке и добавляем ее в список S
        row_sum = sum(row)
        s.append(row_sum)

    return s


# Пример использования программы
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

row_sums = calculate_row_sum(matrix)
print(row_sums)
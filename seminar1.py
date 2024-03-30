def find_element(matrix, target):
    """
    Функция нахождения элемента в 2-мерном массива
    Поиск оптимальный: начинаем с правого верхнего угол
    :param matrix: исходная матрица
    :param target: искомый элемент
    :return: True, если есть в матрице, иначе False
    """
    "с правого верхнего угол"
    row = 0
    col = len(matrix[0]) - 1
    "Условия, чтобы не выйти за пределы матрицы"
    while row < len(matrix) and col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            row += 1  # "Если текущий эл-т меньше - идем вниз"
        else:
            col -= 1  # Если текущий эл-т меньше - идем вниз"
    return False


if __name__ == '__main__':
    # Пример использования:
    matrix = [
        [5, 6, 7],
        [8, 9, 10],
        [11, 12, 13]
    ]
    target = 11
    print(find_element(matrix, target))

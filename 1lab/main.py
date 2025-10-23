

if __name__ == "__main__":
    import random
    n = int(input("Введите количество строк (N): "))
    m = int(input("Введите количество столбцов (M): "))

    if n != m:
        print("Диагонали есть только у квадратных матриц")
    else:
        matrix = [[random.randint(1, 100) for _ in range(m)] for _ in range(n)]

        print("\nМатрица:")
        for stroka in matrix:
            print(stroka)

        print("\nЗначения:")

        max_po_str = [max(stroka) for stroka in matrix]
        print("Максимумы по строкам:", max_po_str)

        max_in_stolb = [max(matrix[i][j] for i in range(n)) for j in range(m)]
        print("Максимумы по столбцам:", max_in_stolb)

        d1_sum = sum([matrix[i][i] for i in range(n)])
        d2_sum = sum([matrix[i][n-i-1] for i in range(n)])
        print("Сумма по диагоналям:", d1_sum, d2_sum)

        str_sums = [sum(stroka) for stroka in matrix]
        max_sum_str_index = str_sums.index(max(str_sums))
        print("Строка с наибольшей суммой:", max_sum_str_index + 1)

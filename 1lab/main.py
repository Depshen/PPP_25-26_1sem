

if __name__ == "__main__":
    import random
    n = int(input("Введите количество строк (N): "))
    m = int(input("Введите количество столбцов (M): "))

    if n != m:
        print("Диагонали есть только у квадратных матриц")
    else:
        matrix = [[random.randint(1, 100) for _ in range(m)] for _ in range(n)]

        print("\nМатрица:")
        for row in matrix:
            print(row)

        print("\nЗначения:")

        max_by_rows = [max(row) for row in matrix]
        print("Максимумы по строкам:", max_by_rows)

        max_in_cols = [max(matrix[i][j] for i in range(n)) for j in range(m)]
        print("Максимумы по столбцам:", max_in_cols)

        row_sums = [sum(row) for row in matrix]
        max_sum_row_index = row_sums.index(max(row_sums))
        print("Суммы по строкам:", row_sums)
        print("Строка с наибольшей суммой:", max_sum_row_index + 1)

        d1_sum = sum([matrix[i][i] for i in range(n)])
        d2_sum = sum([matrix[i][n-i-1] for i in range(n)])
        print(d1_sum, d2_sum)

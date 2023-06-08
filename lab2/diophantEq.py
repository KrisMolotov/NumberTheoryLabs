from sympy import Matrix


def multiply_column_by_negative_one(matr, column_number):
    for i in range(m.shape[0]):
        matr[i, column_number] *= -1


def check_current_row_for_zeros(matr, current_row):
    cols = matr.cols
    for k in range(current_row + 1, cols - 1):
        if matr[current_row, k] != 0:
            return False
    return True


def transform_columns(matr, current_col, source_col, factor):
    matr[:, current_col] -= matr[:, source_col] * factor


def make_unit_matrix(size):
    matr = Matrix.eye(size)
    matr.row_del(size - 1)
    return matr


def make_negative_vector_b(matr):
    vector_b = [-bi for bi in matr[:, -1] * -1]
    return vector_b


def find_minimal_index(current_row):
    make_positive_row = [abs(element) for element in current_row]
    index_of_min = min((i for i, val in enumerate(make_positive_row) if val != 0), key=make_positive_row.__getitem__)
    return index_of_min


def whole_part_of_division(matr, current_row):
    cols = matr.cols
    for i in range(current_row + 1, cols - 1):
        multiplier = matr[current_row, i] // matr[current_row, current_row]
        transform_columns(matr, i, current_row, multiplier)


def create_A_streak(matr):
    rows = matr.rows
    cols = matr.cols
    matr[:, cols - 1] = make_negative_vector_b(matr)
    matr = matr.col_join(make_unit_matrix(cols))
    for i in range(rows):
        while check_current_row_for_zeros(matr, i) == False:
            min_index = find_minimal_index(matr[i, i:cols - 1]) + i
            if matr[i, min_index] == 0:
                continue
            elif matr[i, min_index] < 0:
                multiply_column_by_negative_one(matr, min_index)
            if min_index != i:
                temp_col = matr[:, i].copy()
                matr[:, i] = matr[:, min_index]
                matr[:, min_index] = temp_col
            whole_part_of_division(matr, i)
    return matr


def find_solution(matr, matr_rank):
    solution = []
    for i in range(matr.rows - matr.cols + 1):
        if matr[i, matr.cols - 1] == 0:
            for j in range(matr_rank, matr.cols):
                solution.append(matr[matr.rows - matr.cols + 1:, j].tolist())
            return solution
    return solution


if __name__ == '__main__':
    with open('matrix.txt', 'r') as f:
        matrix = [[int(num) for num in line.split()] for line in f]
    m = Matrix(matrix)
    print("Размерность иходной расширенной матрицы:", m.shape)
    print("Элементы расширенной матрицы:")
    for i in range(m.shape[0]):
        for j in range(m.shape[1]):
            print(m[i, j], end=' ')
        print()
    A_streak = create_A_streak(m)
    matrix_rank = 0
    for i in range(A_streak.rows - A_streak.cols + 1):
        if A_streak[i, i] != 0:
            d = A_streak[i, A_streak.cols - 1] // A_streak[i, i]
            transform_columns(A_streak, A_streak.cols - 1, i, d)
        else:
            matrix_rank = i
            break
        matrix_rank = i + 1
    print("Общее решение системы:")
    print(find_solution(A_streak, matrix_rank))

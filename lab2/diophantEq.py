class DiophantSolver:
    def __init__(self):
        self.rows = 0
        self.number_eqs = int(input("Введите количество уравнений: "))
        self.number_unknowns = int(input("Введите количество неизвестных: "))
        self.matrix = []
        self.extra = []
        for i in range(self.number_eqs):
            print(f"Введите коэффициенты {i + 1}-го уравнения: ", end="")
            line = list(map(int, input().split()))
            if len(line) != self.number_unknowns + 1:
                raise Exception("Incorrect matrix!")
            self.matrix.append(line)
        self.first_part()
        self.second_part()
        self.division()
        self.return_answer()
        self.print()

    def division(self):
        for i in range(0, self.number_eqs - self.number_unknowns + 1):
            if self.matrix[i][i] != 0:
                k = self.matrix[i][self.number_unknowns - 1] // self.matrix[i][i]
                self.subtract(self.number_unknowns - 1, i, k)
            else:
                self.rows = i
                break
            self.rows = i + 1

    def is_zero(self, i):
        for j in range(i + 1, self.number_unknowns - 1):
            if self.matrix[i][j] == 0:
                return True
        return False

    def divide(self, row):
        for i in range(row + 1, self.number_unknowns - 1):
            d = self.matrix[row][i] // self.matrix[row][row]
            self.subtract(i, row, d)

    def subtract(self, i, j, d):
        for k in range(self.number_eqs):
            self.matrix[k][i] -= self.matrix[k][j] * d

    def inversion(self, i):
        for row in self.matrix:
            row[i] = -row[i]

    def swapper(self, i, j):
        for k in range(self.number_eqs):
            temp = self.matrix[k][i]
            self.matrix[k][i] = self.matrix[k][j]
            self.matrix[k][j] = temp

    def check_minimum(self, row, k):
        abs_row = [abs(row[i]) for i in range(k, self.number_unknowns - 1)]
        m = 0
        for x in abs_row:
            if x > 0:
                m = x
                break
        index = abs_row.index(m)
        for i in range(0, len(abs_row)):
            if 0 < abs_row[i] < m:
                m = abs_row[i]
                index = i
        return index + k

    def first_part(self):
        for i in range(self.number_eqs):
            self.matrix[i][self.number_unknowns - 1] = -self.matrix[i][self.number_unknowns - 1]
        for i in range(self.number_unknowns - 1):
            line = [0 for j in range(self.number_unknowns)]
            line[i] = 1
            self.matrix.append(line)
        self.number_eqs += self.number_unknowns - 1

    def second_part(self):
        for i in range(self.number_eqs):
            while not self.is_zero(i):
                index = self.check_minimum(self.matrix[i], i)
                if self.matrix[i][index] == 0:
                    continue
                if self.matrix[i][index] < 0:
                    self.inversion(index)
                if index != i:
                    self.swapper(i, index)
                self.divide(i)

    def return_answer(self):
        for i in range(0, self.number_eqs - self.number_unknowns + 1):
            if self.matrix[i][self.number_unknowns - 1] != 0:
                raise Exception("Error!")
        for j in range(self.rows, self.number_unknowns):
            x = []
            for i in range(self.number_eqs - self.number_unknowns + 1, self.number_eqs):
                x.append(self.matrix[i][j])
            self.extra.append(x)

    def print(self):
        n = self.number_unknowns - 1
        s = len(self.extra)
        for i in range(n):
            print(self.extra[s - 1][i], end="\t")
            for j in range(0, s - 1):
                print(self.extra[j][i], end="\t")
            print()


if __name__ == '__main__':
    DiophantSolver()

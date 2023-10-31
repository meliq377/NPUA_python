class Matrix:
    def __init__(self, n, m):
        self.rows = n
        self.cols = m
        self.matrix = [[i + j for j in range(m)] for i in range(n)]

    def print_matrix(self):
        for row in self.matrix:
            print(row)

    def calculate_mean(self):
        flat_matrix = [element for row in self.matrix for element in row]
        return sum(flat_matrix) / len(flat_matrix)

    def sum_of_row(self, row_index):
        return sum(self.matrix[row_index])

    def average_of_column(self, col_index):
        col_values = [row[col_index] for row in self.matrix]
        return sum(col_values) / len(col_values)

    def print_submatrix(self, col_range, row_range):
        submatrix = [row[col_range[0]:col_range[1] + 1] for row in self.matrix[row_range[0]:row_range[1] + 1]]
        for row in submatrix:
            print(row)
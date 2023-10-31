import random

def generate_random_matrix(n : int, m : int):
    res_mat = []
    for i in range(n):
        col_mat = []
        for j in range(m):
            col_mat.append(random.randint(0, 100))
        res_mat.append(col_mat)
    print(res_mat)
    return res_mat

def get_column_sum(matrix, col_num):
    col_sum = 0
    for i in range(len(matrix)):
        col_sum += matrix[i][col_num]
    print(col_sum)
    return col_sum



def get_row_average(matrix, row_num):
    col_sum = 0
    for i in range(len(matrix[row_num])):
        col_sum += matrix[row_num][i]
    print(col_sum/len(matrix[row_num]))
    return col_sum/len(matrix[row_num])


get_row_average([[1,2,3],
                 [4,5,6],
                 [7,8,9]], 0)








import numpy as np

def calculate_product(vector, matrix):
    result = np.dot(vector, matrix)
    return result

def write_result_to_file(result, filename):
    with open(filename, 'w') as file:
        for row in result:
            file.write(','.join(map(str, row)) + '\n')



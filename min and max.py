import numpy as np

first_input = list(input().split())
n_count = int(first_input[0])
array  = []
for i in range(n_count):
    input_ = input().split()
    array.append(input_)

matrix_array = np.array(array, dtype=int)        
matrix = np.max(np.min(matrix_array, axis=1))
print(matrix)
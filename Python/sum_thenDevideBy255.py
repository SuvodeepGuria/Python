import numpy as np

# Create two matrices
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

# Sum the matrices
summed_matrix = matrix1 + matrix2

# Divide the summed matrix by a scalar (255.0)
result = summed_matrix / 255.0

# Print the result
print(result)

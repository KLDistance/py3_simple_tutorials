import numpy as np

# two methods to declare a matrix
matrix1 = np.matrix([[1,2,3], [4,5,6], [7,8,9]])
matrix2 = np.matrix('1,3,5; 2,4,6; 3,5,7')
print(matrix1)
print(matrix2)
print()

# matrix transpose (memory copy)
print('transpose matrix1')
print(matrix1.transpose())

# matrix trace (memory copy)
print('matrix1 trace')
print(matrix1.trace())

# matrix inverse (memory copy)
print('matrix1 inverse')
print(matrix1.I)

# matrix multiply (memory copy)
print('matrix mul')
print(matrix1 * matrix2)

# diagonalization
print('matrix diagonalization')
eig_val, eig_vec = np.linalg.eig(matrix1)
print('eig_val\n', eig_val, '\neig_vec\n', eig_vec)

# svd
print('matrix SVD')
u, s, v = np.linalg.svd(matrix1)
print('u\n', u, '\ns\n', s, '\nv\n', v)
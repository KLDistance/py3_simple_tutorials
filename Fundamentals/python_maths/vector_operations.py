import numpy as np

# convert a list to a vector
vector1 = np.array([1, 2, 3, 4, 5])
vector2 = np.array([10, 10, 10, 10, 12])
# vector supports direct numerical calculation, which is different from list
vector_addition_res = vector1 + vector2
print(vector_addition_res)
vector_dot_mul_res = vector1 * vector2
print(vector_dot_mul_res)
# this is an inner product
ipres = vector1.dot(vector2)
print(ipres)

# use linspace to create vector values with an equal partition
vector_lins = np.linspace(1, 10, 20)
print(vector_lins)
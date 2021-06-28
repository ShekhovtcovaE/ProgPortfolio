import numpy as np
import time

def mult(arr1, arr2):
  return np.matmul(arr1, arr2)

matrix1 = np.random.rand(3,3)
matrix2 = np.random.rand(3,3)

print(matrix1)
print(matrix2)

start = time.time()
res = mult(matrix1, matrix2)
end = time.time()
print(end - start)

print(res)

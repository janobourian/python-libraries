import numpy as np

a = np.array([[-5, 3], [-7, 4]])
b = np.array([[4, -3], [7, -5]])
c = a @ b
print(f"c: {c}")
d = b @ a
print(f"d: {d}")
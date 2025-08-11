arr = [[0] * 4 for i in range(4)]
print("\n".join(str(j) for j in arr))

print("\nReplaced 0 by -1 at [1,1]: ")
arr[1][1] = -1
print("\n".join(str(j) for j in arr))


import numpy as np

print("\n\nNumpy Ease of use: ")
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\n".join(str(j) for j in arr))
print("\nUpdated matrix for even numbers: ")
arr[arr % 2 == 0] = -1
print("\n".join(str(j) for j in arr))
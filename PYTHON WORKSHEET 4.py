import numpy as np

# Question 1: Array Creation
# 1.1 1D array from 5 to 25
arr1d = np.arange(5, 26)
print("1.1:", arr1d)

# 1.2 2D array (3x4), random integers between 10 and 50
arr2d = np.random.randint(10, 51, size=(3, 4))
print("1.2:\n", arr2d)

# Question 2: Array Attributes
print("2.1 Shape:", arr1d.shape)
print("2.1 Size:", arr1d.size)
print("2.1 Data type:", arr1d.dtype)

print("2.2 Shape:", arr2d.shape)
print("2.2 Size:", arr2d.size)
print("2.2 Data type:", arr2d.dtype)

# Question 3: Array Operations
array1 = np.array([2, 4, 6, 8, 10])
array2 = np.array([1, 3, 5, 7, 9])

print("3.2 Addition:", array1 + array2)
print("3.2 Subtraction:", array1 - array2)
print("3.2 Multiplication:", array1 * array2)
print("3.2 Division:", array1 / array2)

# Question 4: Broadcasting
arr_2d = np.arange(1, 10).reshape((3, 3))
print("4.1:\n", arr_2d)
print("4.2 Multiplied by 5:\n", arr_2d * 5)

# Question 5: Slicing and Indexing
arr4x4 = np.arange(10, 26).reshape((4, 4))
print("5.1:\n", arr4x4)
print("5.2 Second row:", arr4x4[1])
print("5.2 Last column:", arr4x4[:, -1])
arr4x4[0] = 0
print("5.3 First row replaced with zeros:\n", arr4x4)

# Question 6: Boolean Indexing
arr_bool = np.random.randint(20, 41, size=10)
print("6.1:", arr_bool)
print("6.2 Elements > 30:", arr_bool[arr_bool > 30])

# Question 7: Reshaping
arr_1d12 = np.arange(11, 23)
arr_2d3x4 = arr_1d12.reshape((3, 4))
print("7.1:", arr_1d12)
print("7.2 Reshaped (3x4):\n", arr_2d3x4)



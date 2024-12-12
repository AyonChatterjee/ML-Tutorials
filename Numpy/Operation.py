import numpy as np

a = np.array([[1 , 2],
              [3 ,4]])

b = np.array([[4,3],[2,1]])


print("Adding 1 to every element: ", a + 1)


print("\nSubstracting 2 to every element:\n ", b - 2)

print("\nSum of all array elements:", a.sum())

print("\nArray sum:\n" , a + b)


# Adding 1 to every element:  [[2 3]
# [4 5]]

# Substracting 2 to every element:
# [[ 2  1]
# [ 0 -1]]

# Sum of all array elements: 10

# Array sum:
# [[5 5]
# [5 5]]
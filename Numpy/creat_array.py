import numpy as np 

arr = np.array([1 , 2 , 3])
print("Array with Rank 1:" , arr)

arr = np.array([[1, 2, 3],
                [4, 5, 6]])
print("Array with Rank 2: \n", arr)

arr = np.array((1 , 3, 2))
print("Array created using tuple:" , arr)

#  Output :   
#  Array with Rank 1: [1 2 3]
#  Array with Rank 2: 
#  [[1 2 3]
#  [4 5 6]]
#  Array created using tuple: [1 3 2]
import pandas as pd
ser = pd.Series(range(1 , 20 , 3) , index = [x for x in 'abcdefg'])
print(ser)

# Output:
# a    1
# b     4
# c     7
# d    10
# e    13
# f    16
# g    19
# dtype: int64


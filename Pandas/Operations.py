import pandas as pd

# def add_values(row):
#     return row['A'] + row['B'] + row['C']

# def main():
#     # Create a dictionary with three fields each
#     data = {
#         'A': [1 , 2 , 3] , 
#         'B': [4 , 5 , 6] ,
#         'C': [7 , 8 , 9]}

#     df = pd.DataFrame(data)

#     df['Add'] = df.apply(add_values , axis = 1)
    
#     print(df)

# if __name__ =='__main__':
#     main()

# Output : 
#   A  B  C  Add
# 0  1  4  7   12
# 1  2  5  8   15
# 2  3  6  9   18    


def add(a , b , c):
    return a + b + c

def main():
   
    data = {
        'A' : [1 , 2 , 3] , 
        'B' : [4 , 5 , 6] , 
        'C' : [7 , 8 , 9]}

    # coverting the dictionary into dataframe
    df = pd.DataFrame(data)

    df['add'] = df.apply(lambda row : add(row['A']  , row['B'] , row['C']) , axis = 1)

    print(df)

if __name__ == '__main__':
  main()


# Output :
#    A  B  C  add
# 0  1  4  7   12
# 1  2  5  8   15
# 2  3  6  9   18
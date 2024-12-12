import pandas as pd

data ={'Name' : ['Ayon' , 'Arun', 'Arjun' , 'Anuj'],
       'Age' : [27 , 28 , 22 , 21], 
       'Address':['Delhi' , 'Goa', 'Kanu' , 'New'],
       'Qualification':['Msc' , 'MA' , 'BA' , 'BTECH']}

df = pd.DataFrame(data)


print(df[['Name' , 'Age']])

# Output :
#     Name  Age
# 0   Ayon   27
# 1   Arun   28
# 2  Arjun   22
# 3   Anuj   21
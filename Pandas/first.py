import pandas as pd 

# list of Strings
# list = ['Geeks' , 'For' , 'Geeks' , 'is' , 'portal' , 'for' , 'Geeks']

# df = pd.DataFrame(list)
# print(df)



# Output:
# 0   Geeks
# 1     For
# 2   Geeks
# 3      is
# 4  portal
# 5     for
# 6   Geeks



# Adding a column in pandas dataFrame 

# Defining a dictionary 
data = {'Name':['Ayon' , 'Ankit' , 'Gaurav' , 'Anuj'], 
        'Height':[5.1 , 5.6 , 6.0 , 5.8], 
        'Qualification':['Msc' , 'MA' , 'MBA' , 'BTECH']}

# convert the dictionary into the dataframe
df = pd.DataFrame(data)

# Declare a list that is to be coverted into a column
Address = ['Delhi' , 'Mumbai' , 'Punjab' , 'Chennai']

# Using 'Address' as the column name
df['Address'] = Address

print(df)

#      Name  Height Qualification  Address
# 0    Ayon     5.1           Msc    Delhi
# 1   Ankit     5.6            MA   Mumbai
# 2  Gaurav     6.0           MBA   Punjab
# 3    Anuj     5.8         BTECH  Chennai


import pandas as pd 

data  = pd.DataFrame({'Brand': ['Maruti', 'Hyundai', 'Tata', 
                               'Mahindra', 'Maruti', 'Hyundai', 
                               'Renault', 'Tata', 'Maruti'], 
                     'Year': [2012, 2014, 2011, 2015, 2012, 
                              2016, 2014, 2018, 2019], 
                     'Kms Driven': [50000, 30000, 60000, 
                                    25000, 10000, 46000, 
                                    31000, 15000, 12000], 
                     'City': ['Gurgaon', 'Delhi', 'Mumbai', 
                              'Delhi', 'Mumbai', 'Delhi', 
                              'Mumbai', 'Chennai',  'Ghaziabad'], 
                     'Mileage':  [28, 27, 25, 26, 28, 
                                  29, 24, 21, 24]})

# print(data)

# Output
#      Brand  Year  Kms Driven       City  Mileage
# 0    Maruti  2012       50000    Gurgaon       28
# 1   Hyundai  2014       30000      Delhi       27
# 2      Tata  2011       60000     Mumbai       25
# 3  Mahindra  2015       25000      Delhi       26
# 4    Maruti  2012       10000     Mumbai       28
# 5   Hyundai  2016       46000      Delhi       29
# 6   Renault  2014       31000     Mumbai       24
# 7      Tata  2018       15000    Chennai       21
# 8    Maruti  2019       12000  Ghaziabad       24


# Using loc() method 

# print(data.loc[(data.Brand == 'Maruti') & (data.Mileage > 25)])
#    Brand  Year  Kms Driven     City  Mileage
# 0  Maruti  2012       50000  Gurgaon       28
# 4  Maruti  2012       10000   Mumbai       28

# Selecting a range of rows from the dataframe
# print(data.loc[2:5])
#      Brand  Year  Kms Driven    City  Mileage
# 2      Tata  2011       60000  Mumbai       25
# 3  Mahindra  2015       25000   Delhi       26
# 4    Maruti  2012       10000  Mumbai       28
# 5   Hyundai  2016       46000   Delhi       29

# Updating the value of any column
# data.loc[(data.Year < 2015) , ['Mileage']] = 22
# print(data)
#       Brand  Year  Kms Driven       City  Mileage
# 0    Maruti  2012       50000    Gurgaon       22
# 1   Hyundai  2014       30000      Delhi       22
# 2      Tata  2011       60000     Mumbai       22
# 3  Mahindra  2015       25000      Delhi       26
# 4    Maruti  2012       10000     Mumbai       22
# 5   Hyundai  2016       46000      Delhi       29
# 6   Renault  2014       31000     Mumbai       22
# 7      Tata  2018       15000    Chennai       21
# 8    Maruti  2019       12000  Ghaziabad       24



# Using the iloc() function
# print(data.iloc[[0 , 2 , 5 , 7]])
#     Brand  Year  Kms Driven     City  Mileage
# 0   Maruti  2012       50000  Gurgaon       28
# 2     Tata  2011       60000   Mumbai       25
# 5  Hyundai  2016       46000    Delhi       29
# 7     Tata  2018       15000  Chennai       21

# print(data.iloc[1 : 5 , 2 : 5])(Selecting rows from 1 to 4 and columns from 2 to 4)
#    Kms Driven    City  Mileage
# 1       30000   Delhi       27
# 2       60000  Mumbai       25
# 3       25000   Delhi       26
# 4       10000  Mumbai       28
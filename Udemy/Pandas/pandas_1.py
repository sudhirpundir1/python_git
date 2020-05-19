import pandas as pd
pd.set_option('display.max_rows',500)
pd.set_option('display.max_columns',50)
pd.set_option('display.width',300)

df = pd.read_csv('original.csv',delimiter=',')
#df.info()
print(df)
#display first 5 rows
print(df.head(5))
#display the share of data rows and columns
print(df.shape)

#display number of rows in 0th column
print(df.shape[0])
# Selecting a column from the dataframe
#display number of rows below columns
print(df.Country, df.Population)
print(df[['Country','Population']])

#to flter a Rows
print(df.loc[8]) # displays 8th index row data
print(df.loc[[0,5,8]]) # displays 0,5 and 8th index row data
print('***',df.loc[[0,5,8],['Country','Region','Population']]) # displays 0,5 and 8th index row data with selected data
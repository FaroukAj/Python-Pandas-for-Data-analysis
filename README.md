# Python-Pandas-for-Data-analysis
Using python Pandas to load, clean and wrangle data



import pandas as pd
import numpy as np
from pandas.core.indexes.base import Index
from pandas.io.pytables import IndexCol

#import the pandas library and aliasing as pd
data = np.array(['a','b','c','d'])
s = pd.Series(data)
print (s)

dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98] , }

#CREATING A PANDAS DATAFRAME
df = pd.DataFrame(dict)
print(df)

#CHANGING OUR PANDAS DATAFRAME INDEX
df2 = pd.DataFrame(dict ,index = [1,2,3,4,5])
print("New Index: ",df2)

#GETTING THE LOCATION OF A VALUE IN OUR DATAFRAME
df3 = df2.loc[2]
print("2nd value :",df3)

#READING A CSV FILE

df4 = pd.read_csv('survey.csv')
print(df4)

#GETTING THE FIRST 50 ITEMS OF OUR FILE
df5 = df4.head(50)
print(df5)

df5b = df4.tail(20)
print(df5b) #GETTING THE LAST 20 ROWS OF OUR FILE

#OPENING A JSON FILE
df6 = pd.read_json('sample4.json')
print(df6) 

#READING A SQLITE3 FILE
import sqlite3
conn = sqlite3.connect('flacko.db')
c = conn.cursor()
df7 =  pd.read_sql_query('SELECT * FROM flacko' ,conn)
print(df7)

#CONVERTING BACK TO CSV, JSON AND SQL FILE

df8 = df6.to_csv('help.csv') #CONVERTING OUR JSON FILE TO CSV
df9 = df7.to_json('help2.json') #CONVERTING OUR SQL FILE TO JSON
#df10 = df4.to_sql('help3', conn) #ADDINGFILE TO OUR DATBASE

#GETTING INFO ON OUR DATA
df11 = df4.info()
print(df11)

#GETTING THE NUMBER OF ROWS AND COLUMN OF OUR DATA
df12 = df4.shape
print(df12)

#REMOVING DUPLICATE DATAS IN OUR DATA
df13 = df4.drop_duplicates()
print(df13)

df13b = df4.dropna() #DROPPING NOT A NUMBER VALUES
print(df13b)

df14 = pd.read_csv("nba.csv")
new_index = range(1, 456)
df14.reindex(new_index)
df15 = df14.groupby(['Name']) #GETTING VALUES FROM A SPECIFIC COLUMN
df16=  df14.groupby(['Team' , 'Position']) #GROUPING BY TEAM AND GETTING PLAYERS BY POSITION
print(df16.last())#PRINTING THE FIRST ITEMS IN THE GROUP
print(df16.all()) #SEEING IF THE COLUMNS IN THE GROUP EXIST
#print(df14)
print(df15.all())#PRINTING ALL VALUES BY THE GROUP OF NAME

print(df.describe()) #TO GET SOME INTUITION ABOUT OUR DATAFRAME
col = df14['Salary'] #GETTING A COLUMN FROM OUR DATA
print("Salary :" , col) 

df14['Veteran'] = df14['Age'] >= 27 #ADDING A COLUM TO OUR DATA
col2 = df14[['Salary', 'Age' , 'Name', 'Veteran']]#SELECTING MULTIPLE COLUMNS
print(col2)

#CONVERTING A PANDAS SERIES TO A NUMPY ARRAY
col3 = df14['Salary'].values
print("Pandas to Numpy :" , col3)


#GETTING THE LAST 3 LOWEST SALARY
least_paid =  df14.nsmallest(3, 'Salary')

print("Three lowest paid players :" , least_paid)

#GETTING THE 3 HIGHEST SALARY

highest_paid = df14.nlargest(3 , 'Salary')
print("Three highest paid players :" , highest_paid)

#USING ILOC TO LOCATE A DATA IN A DATAFRAME

player = df14.iloc[3]
print ("Your selection : " ,player)

#PRINTING DATAS WITH NA :
df_nan = df14[df14.isna().any(axis=1)]
print(df_nan)

#PRINTING DATA WITH CERTAIN STTRINGS WE WANT TO FIND E.G WE WILL PRINT EVERY DATA WITH PLAYERS THAT WENT TO A COLLEGE THAT STARTS WITH 'BO'
df_bos = df14[df14['College'].str[0:2] == 'Bo']
print(df_bos.head())

#CHANGING DATA TYPE WITH AS.TYPE AND PD.TO_NUMERIC/PD.TO_STRING
df14['Salary'].astype(np.float32) # HERE WE CHANGE THE DATA IN THE SALARY COLUMN TO FLOAT DATA TYPE USING AS.TYPE
df14['Number'] = pd.to_numeric(df14['Number'])# HERE WE CHANGE THE DATA IN THE NUMBER COLUMN TO NUMERIC DATA TYPE USING PD.TO_NUMERIC

print(df14)

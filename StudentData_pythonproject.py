#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import datetime
import os





# In[5]:


data = pd.read_csv('student_data-2 copy.csv')


data.describe()


# In[ ]:


#Check for missing values 
data.isnull().sum()


# In[97]:


data.head(50)


# In[44]:


#Calculate the average age of students in each specialization.


#CONVERT 'Date_of_Birth' column from string to date datatype :

data['Date_of_Birth'] = pd.to_datetime(data['Date_of_Birth'])

#ADD A NEW COLUMN CALLED AGE :
now = datetime.datetime.now()
current_year = now.year 
data['Age']= current_year - pd.DatetimeIndex(data['Date_of_Birth']).year


Avg_age = data.groupby(data['Specialization'])['Age'].mean()


print(Avg_age)


# In[45]:


#Retrieve the total number of students in each field of study.
Total_students = data.groupby('Field_of_Study')['Student_ID'].nunique()
print(Total_students)


# In[96]:


#Find the number of students who are expected to graduate in each year.


grad_students = data.groupby(data['Expected_Year_of_Graduation'])['Student_ID'].nunique()
print(grad_students)
        
#graduating_students()

gs = pd.DataFrame({'Year_of _Gradution' : grad_students.index,  'Students' : grad_students.values})
#graduation = gs['Year_of _Gradution']

gs.plot(kind = 'line', x = 'Year_of _Gradution' , y = 'Students', color = 'blue', marker = '*')
plt.xlabel('Year of Graduation')
plt.ylabel('Number of students')
plt.ylim(28000, 29000)
plt.show()


# In[56]:


#Determine the total fees collected for each year of admission.

Total_fees = data.groupby('Year_of_Admission')['Fees'].sum()
#print(Total_fees)


Tf = pd.DataFrame({'Year_of_Admission': Total_fees.index, 'Fees': Total_fees.values})

fee = Tf['Fees'].values.tolist()
#print(fee)
yearr = Tf['Year_of_Admission'].values.tolist()
#print(yearr)

#Visualization
colors = ['Blue' , 'Green', 'Yellow', 'Orange' , 'Indigo', 'Violet', 'Red']
Tf.plot(kind= 'bar', x = 'Year_of_Admission', y ='Fees', color = colors)
plt.xlabel ('Year of Admission')
plt.ylabel('Total Fees in millions')
plt.show()



# In[59]:


#Calculate the average discount on fees for each field of study.

avg_discount = data.groupby('Field_of_Study')['Discount_on_Fees'].mean()
Rounded_discount = round(avg_discount , 2)
print(Rounded_discount)


# In[70]:


#Identify the student(s) with the highest discount on fees.

student_discount = data.groupby('Student_ID')['Discount_on_Fees'].sum()
#print(student_discount)

sd = pd.DataFrame(student_discount)

top_five =  sd.nlargest(5, 'Discount_on_Fees')
print(top_five)


# In[83]:


#Find the field of study with the highest total fees collected.

highest_fees = data.groupby('Field_of_Study')['Fees'].sum()
hs = pd.DataFrame({'Field': highest_fees.index ,  'Total_fees' : highest_fees.values})
print(hs)

#VISUALIZATION

hs.plot(kind = 'bar' , x = 'Field', y =  'Total_fees', color = ('blue', 'green', 'orange', 'yellow', 'Violet'), )
plt.xlabel('Field')
plt.ylabel('Total Fees in Billions')
plt.title('highest total fees per field')
plt.show()


# In[114]:



#Identify the students who have the same field of study, specialization, and expected year of graduation.
grouped_students = data.groupby(['Field_of_Study', 'Specialization', 'Expected_Year_of_Graduation'])['Student_ID'].nunique()

# Filter the groups where the count of unique student IDs is greater than 1
same_students = grouped_students[grouped_students > 0]
same_students = pd.DataFrame(same_students)
same_students = same_students.sort_values(by = ['Expected_Year_of_Graduation'])

pd.set_option('display.max_rows', None)
same_students.head(100)


# In[ ]:





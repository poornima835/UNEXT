#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


data={
    "names":['a','b','c'],
    "ages":[25,28,21]
}


# In[5]:


df=pd.DataFrame(data)


# In[6]:


df


# In[7]:


print(df)


# In[8]:


df.head(2)


# In[9]:


df.tail(3)


# In[11]:


print(df.tail(1))


# In[12]:


df.dtypes


# In[13]:


df.info


# In[ ]:


#rename the column name


# In[15]:


df.columns=["emp_name",'age']
df


# In[18]:


df2=df.rename(columns={"emp_name":"emp_first_name","age":"emp_age"})


# In[19]:


df2


# In[20]:


dept=["sales","Marketing","IT"]
df.assign(Company=dept)


# In[23]:


df2.dtypes


# In[24]:


#convert integer to a string 
df3=df2.convert_dtypes()


# In[27]:


df3.dtypes


# In[30]:


df4=df2.astype({"emp_age":float})


# In[31]:


df4


# In[32]:


#count rows of data frame
len(df2)


# In[34]:


#count rows of data frame
df2.shape[0]


# In[35]:


#count columns of data frame
df2.shape[1]


# In[36]:


#to get rows and columns
df2.shape


# New datafram

# In[44]:


index_label=('r1','r2','r3','r4')


# In[37]:


technologies = {
    'Courses':["Spark","PySpark","Hadoop","Python","pandas"],
    'Fee' :[20000,25000,26000,22000,24000],
    'Duration':['30day','40days','35days','40days','60days'],
    'Discount':[1000,2300,1200,2500,2000]
              }


# In[39]:


df=pd.DataFrame(technologies)
df


# In[51]:


#df=pd.DataFrame(technologies,index=index_label)


# In[42]:





# In[49]:


df.query=("Courses!='PySpark'")


# In[47]:


df


# In[55]:


df=pd.read_csv('employees.csv')
df


# In[ ]:





# In[ ]:





# In[ ]:





# In[59]:


emp_df["Start Date"]=pd.to_datetime(emp_df["Start Date"])


# In[ ]:


emp_df


# In[ ]:


emp_df.nunique()


# In[ ]:





# In[61]:


import numpy as np


# In[63]:


arr=np.array([1,2,3])


# In[64]:


arr


# In[67]:


arr2=np.array([[1,23,33],
               [2,22,54]])


# In[68]:


arr2


# In[71]:


arr3=np.array([[[1,23,33],[2,22,54],[5,6,8]],[[10,20,30],[25,22,55],[50,60,80]]])


# In[72]:


arr3


# In[73]:


arr[1]


# In[76]:


arr[0:2]


# In[77]:


arr2[0,-1]


# In[79]:


arr3[0,1,2]


# In[7]:


#slicing indexing##
import numpy as np


# In[8]:


temperature_data = [25.3, 26.1, 24.8, 23.5, 27.2]
pressure_data = [101.2, 100.8, 101.5, 100.2, 101.0]
humidity_data = [55.2, 54.8, 56.5, 53.7, 55.9]


# In[9]:


#calculate numpy array for them 
temperature_array=np.array(temperature_data)
pressure_array=np.array(pressure_data)
humidity_array=np.array(humidity_data)


# In[ ]:





# In[10]:


##standard deviation 
temperature_std=np.std(temperature_array)


# In[11]:


temperature_std


# MatPlotLib

# In[16]:


import matplotlib.pyplot as plt


# In[17]:


x_axis=np.array([1,10])
y_axis=np.array([1,50])


# In[18]:


plt.plot(x_axis,y_axis)


# In[20]:


y_points=np.array([1,10,2,8,5])
plt.plot(y_points)


# In[31]:


y_points=np.array([1,10,2,8,5])
plt.plot(y_points,marker='o', color='purple')
plt.xlabel("x-axis")
plt.ylabel("y-axis")


# In[39]:


months=['January', 'February', 'March', 'April', 'May']


# In[40]:


months


# In[41]:


sales=[2500, 3200, 2800, 4100, 3700]


# In[43]:


plt.bar(months,sales, color='purple')
plt.xlabel('Months')
plt.ylabel('Sales')


# In[44]:


plt.savefig("month.png")


# In[45]:


plt.show()


# In[ ]:





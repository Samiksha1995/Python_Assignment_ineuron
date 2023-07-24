#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[4]:


df=pd.read_csv(r"C:\Users\mahaj\OneDrive\Desktop\Python_Diwali_Sales_Analysis\Diwali Sales Data.csv", encoding= 'unicode_escape')


# In[5]:


df.head()


# In[8]:


df.shape


# In[9]:


df.info()


# In[11]:


#Drop the unrelated and blank counmns
df.drop(['Status','unnamed1'],axis=1,inplace=True)
#axis=1 :all row related to that columns
#inplace:Save the content or implement it in given dataframe 


# In[12]:


df.info()


# In[14]:


#Check the null values
df.isnull().sum()


# In[16]:


df.shape


# In[17]:


#drop null values
df.dropna(inplace=True)


# In[18]:


df.shape


# Change data Type

# In[19]:


df['Amount']=df['Amount'].astype('int')


# In[21]:


df['Amount'].dtype


# In[22]:


df.columns


# In[23]:


#Rename Columns
df.rename(columns={'Marital_Status':'shaadi'})


# In[24]:


#describe() method returns the description of the data in a dataframe (ie. count, mean ,std etc)
df.describe()


# In[26]:


#use describe() for specific columns
df[['Age','Orders','Amount']].describe()


# # Exploratory Data Analysis

# In[29]:


df.columns


# In[30]:


sns.countplot(x='Gender',data=df)


# # Gender

# In[34]:


ax=sns.countplot(x='Gender',data=df)
for bars in ax.containers:
    ax.bar_label(bars)


# In[36]:


sales_gen=df.groupby(['Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sns.barplot(x='Gender',y='Amount',data=sales_gen)


# From above graphs we can see that most of the buyers are females and even the purchasing power of female is greater than men

# # Age

# In[38]:


ax=sns.countplot(x='Age Group',data=df,hue='Gender')
for bars in ax.containers:
    ax.bar_label(bars)


# In[39]:


#Total amount V/s Age group
sales_Age_Group=df.groupby(['Age Group'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sns.barplot(x='Age Group',y='Amount',data=sales_Age_Group)


# Most of the buyer are in the age group of 26 to 35 and most of are women

# # State

# In[40]:


#total number of order by top 10 state
sales_state=df.groupby(['State'],as_index=False)['Orders'].sum().sort_values(by='Orders',ascending=False).head(10)
sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data=sales_state,x='State',y='Orders')


# In[6]:


#total amount spend by top 10 state
sales_state=df.groupby(['State'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False).head(10)
sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data=sales_state,x='State',y='Amount')


# From the above graphs we cam see that most of the orders and amount spend by UP,Mahatashtra & Karnataka

# #Marital Status

# In[8]:


df.columns


# In[11]:


sns.set(rc={'figure.figsize':(8,5)})
ax=sns.countplot(x='Marital_Status',data=df)
for bars in ax.containers:
    ax.bar_label(bars)


# In[17]:


sales_state=df.groupby(['Marital_Status','Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False).head(10)
sns.barplot(data=sales_state,x='Marital_Status',y='Amount',hue='Gender')


# From the above graph we can say tha most of money is spend by married women

# # Occupation        

# In[20]:


sns.set(rc={'figure.figsize':(20,5)})
ax=sns.countplot(data=df,x='Occupation')
for bars in ax.containers:
    ax.bar_label(bars)


# In[18]:


#total amount spend by top occupatiom
sales_state=df.groupby(['Occupation'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False).head(10)
sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data=sales_state,x='Occupation',y='Amount')


# From the above graph we can see that most of buyer are working in IT,Banking and Aviation sector also spend more money on shopping

# # Product Category

# In[24]:


sns.set(rc={'figure.figsize':(20,5)})
ax=sns.countplot(x='Product_Category',data=df)
for bars in ax.containers:
    ax.bar_label(bars)


# In[28]:


sales_Product_cat=df.groupby(['Product_Category'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False).head(10)
sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data=sales_Product_cat,x='Product_Category',y='Amount')


# In[31]:


sales_Product_id=df.groupby(['Product_ID'],as_index=False)['Orders'].sum().sort_values(by='Orders',ascending=False).head(10)
sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data=sales_Product_id,x='Product_ID',y='Orders')


# # Conclusion:

# Married women age group 26-35 yrs from UP,Maharashtra,Karnataka working in IT,Healthcare, and aviation are more likely to buy a products from food,clothing and electronic category

# In[ ]:





# In[ ]:





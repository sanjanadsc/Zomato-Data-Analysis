#!/usr/bin/env python
# coding: utf-8

# # 1. Import Libraries

# In[1]:


import pandas as pd #data manipulation and analyis
import numpy as np #numerical operations
import matplotlib.pyplot as plt #data visualization
import seaborn as sns #data visualization


# # 2. Import dataset

# In[2]:


df= pd.read_csv("Zomato data .csv")
df


# In[3]:


df.info()


# # 2.Convert datatype of coloumn- rate

# In[4]:


def handleRate(value):
    value= str(value).split('/')
    value= value[0];
    return float(value)
df['rate']=df['rate'].apply(handleRate)
df.head()


# # 3.Type of restaurant

# In[5]:


df.head()


# In[6]:


sns.countplot(x=df['listed_in(type)'])
plt.xlabel('Type of resturant')


# # Majority of the resturant falls in dinning category

# # 4.Vote count of the each resturant

# In[7]:


df.head()


# In[8]:


gdf= df.groupby('listed_in(type)')['votes'].sum()
result = pd.DataFrame({'votes': gdf})
plt.plot(result, c='green', marker='o')
plt.xlabel("resturant on the basis of votes", c='red',size=20)
plt.ylabel("votes", c ='red', size=20)


# # Dinning resturants has maximum votes

# # 5. Ratings

# In[9]:


df.head()


# In[10]:


plt.hist(df['rate'],bins=5)
plt.title('ratings distribution')
plt.show


# # majority ratings are 3.5 to 4

# # 6.Average order spending

# In[11]:


df.head()


# In[12]:


sdf=df['approx_cost(for two people)']
sns.countplot(x=sdf)


# # Approximate cost is Rs.300

# # 7.Mode of ratings

# In[13]:


df.head()


# In[14]:


plt.figure(figsize=(6,6))
sns.boxplot(x= 'online_order', y= 'rate', data= df)


# # 8.online order has maximum ratings than offline order

# In[15]:


df.head()


# # 9.Heatmap 

# In[19]:


pivot_table= df.pivot_table(index='listed_in(type)', columns='online_order', aggfunc='size', fill_value=0)
sns.heatmap(pivot_table, annot= True , cmap='YlOrBr', fmt='d')
plt.title('Heatmap')
plt.xlabel("Online Order")
plt.ylabel('Listed In (Type)')
plt.show()


# # Dining restaurants primarily accept offline orders, whereas cafes primarily receive online orders. This suggests that clients preferred orders in person at restaurants, but prefer online ordering at cafes

# In[ ]:





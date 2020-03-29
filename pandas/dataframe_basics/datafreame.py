#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
df = pd.read_csv('weather_data.csv')
df


# In[5]:


df.shape # 6 rows and 4 column


# In[6]:


rows, columns = df.shape


# In[7]:


rows, columns


# In[8]:


df.head()


# In[9]:


# if you want to print few rows then you process
df.head(3)


# In[10]:


# If you want to print last five rows then you process
df.tail()


# In[11]:


# if you want to print last 1 rows then...
df.tail(1)


# In[12]:


df[2:5] # if you want to print 2 to 4 rows then....


# In[13]:


# If you want to print everythings then.....
df[:]


# In[14]:


# If want to print columns then ....
df.columns


# In[23]:


# for printing individual column
df['day'] # or df.day both are same
# df.event


# In[24]:


# For print only two columns
df[['event', 'day']]


# In[26]:


df['temperature'].max()


# In[27]:


df.describe()


# In[29]:


df[df.temperature >= 32]


# In[30]:


df[df.temperature == df.temperature.max()]


# In[32]:


df[['day', 'temperature']][df.temperature == df['temperature'].max()]


# In[33]:


df


# In[34]:


df.index


# In[41]:


df.set_index('day', inplace=True)


# In[42]:


df


# In[43]:


df.reset_index(inplace=True)


# In[44]:


df


# In[48]:


df.set_index('event', inplace=True)
df.loc['Snow']


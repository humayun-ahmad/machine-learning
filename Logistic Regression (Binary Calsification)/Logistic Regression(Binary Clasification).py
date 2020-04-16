#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df = pd.read_csv('book1.csv')
df.head(3)


# In[8]:


plt.scatter(df.age, df.bought_insurance, marker="+", color='red')


# In[10]:


from sklearn.model_selection import train_test_split


# In[13]:


X_train, X_test, y_train, y_test = train_test_split(df[['age']], df.bought_insurance,train_size=.9)


# In[16]:


from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train, y_train)


# In[20]:


print(X_test)
model.predict(X_test)


# In[21]:


model.score(X_test,y_test)


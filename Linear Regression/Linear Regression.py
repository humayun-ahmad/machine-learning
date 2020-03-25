#!/usr/bin/env python
# coding: utf-8

# In[8]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (20.0, 10.0)

#Reading Data
data = pd.read_csv('headbrain.csv')
print(data.shape)
data.head()


# In[9]:


# Collecting X and Y
X = data['Head Size(cm^3)'].values
Y = data['Brain Weight(grams)'].values


# In[11]:


#Mean X and Y
mean_x = np.mean(X)
mean_y = np.mean(Y)

#Total number of values
m = len(X)

#Using the formula to calculate b1 and b0
numer = 0
denom = 0

for i in range(m):
    numer += (X[i] - mean_x)*(Y[i] - mean_y)
    denom += (X[i] - mean_x) ** 2
    
b1 = numer/denom
b0 = mean_y - b1*mean_x
print(b1, b0)


# In[24]:


#plotring values and Regression Line
max_x = np.max(X) + 100
min_x = np.min(X) - 100
# print(max_x, min_x)
#Calculating line values x and y
x = np.linspace(min_x,max_x,1000)
y = b0 + b1 * x
# print(y)

#Plotting Line
plt.plot(x,y,color='#58b970', label = 'Regression Line')

#Plotting Scatter Points
plt.scatter(X,Y, c = '#ef5423', label = 'Scatter Plot')

plt.xlabel('Head Size in cm3')
plt.ylabel('Brain Weight in grams')
plt.legend()
plt.show()



# In[25]:


ss_t = 0
ss_r = 0
for i in range(m):
    y_pred = b0 + b1 * X[i]
    ss_t += (Y[i] - mean_y) ** 2
    ss_r += (Y[i] - y_pred) ** 2
    
r2 = 1 - (ss_r/ss_t)
print(r2)


# In[ ]:





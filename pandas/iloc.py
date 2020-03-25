# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 07:30:12 2020

@author: humayun
"""


import pandas as pd

df = pd.DataFrame([[1,2],[4,5],[7,8]], index = ['raju', 'ravi', 'dani'], columns=['exp','salary'])

print(df.iloc[0])
print(df.iloc[[0]])
print(df.iloc[1])
print(df.iloc[[1]])

print(df.iloc[:1])
print(df.iloc[1:])
print(df.iloc[1:2])

print(df.iloc[0:1])
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 01:30:45 2020

@author: humayun
"""
import numpy as np
np.random.seed(0) #if we change the seed vale the output will be changed otherwise the output will be the same value.
p = np.random.randint(10, size = 5)
print(p)


np.random.seed(1) 
p = np.random.randint(10, size=5)
print(p)


# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 10:36:12 2016

@author: kylerlittle
"""
import numpy as np
x = np.ones(5)
y = np.diag((x))
z = np.arange(3,6,1)
y[0:2,2:5] = z
y[2:5,0:2] = 2
p = -(np.pi)*(np.ones(3))
y[2:5,2:5] = np.diag((p))
print y

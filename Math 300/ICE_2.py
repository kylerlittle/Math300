# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 11:05:28 2016

@author: kylerlittle
"""
import numpy as np
def s(N):
    x = np.zeros(N)
    for i in np.arange(1,N):
        x[i-1] = 1/(i**2)
    return sum(x)
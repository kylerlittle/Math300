# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 19:53:34 2016

@author: kylerlittle
"""
#EXAMPLE FUNCTION- not apart of ICE_6
def f(x):
    p = 4*(x**3)
    return p
#EXAMPLE FUNCTION- not apart of ICE_6

import numpy as np
def midpoint(f,a,b,n):
    if n<=0:
        print "Error: n must be nonzero and positive."
        return False
    a = float(a) 
    b = float(b) #floating a and b makes it so h and x can actually be calculated
    h = (b-a)/n #I defined h in this way so x could be created
    x = np.arange(a,b+h,h)
    w = np.zeros(n)
    k = np.zeros(n)
    for i in np.arange(0,n,1): #NOTE: not doing n-1 since arange function automatically goes from 0 to n-1
        k[i] = (x[i]+x[i+1])/2
        w[i] = (f(k[i]))*h
        j = sum(w)
    return j
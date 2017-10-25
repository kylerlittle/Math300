# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 10:17:36 2016

@author: kylerlittle
"""
import numpy as np
def trapezoid(fct,a,b,n):
  if n<0 or n==0:
    print "Error: n must be positive"
    return False
  h = (np.double(b)-np.double(a))/np.double(n)
  x = np.arange(a,b+h,h)
  y = 2.0*fct(x)
  y[0] = y[0]/2.0
  y[n] = y[n]/2.0
  return sum(y)*h/2.0
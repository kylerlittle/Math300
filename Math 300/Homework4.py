# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 10:08:16 2016

@author: kylerlittle
"""
from trapapprox import trapezoid
import scipy as sp
import pylab as pl
def f(x):
    y = (-1./6.) + x + ((-1./24.)*x**2) + ((-1./6.)*x**3) + ((5./96.)*x**4)
    return y  
def name_integral(a,b):
    x = sp.integrate.quad(f,a,b)
    x = sp.asarray(x)
    return x[0]
diff = sp.zeros(6)
n = sp.array([10,100,1000,10000,100000,1000000],dtype=sp.double)
n_ln = sp.arange(6, dtype=sp.double)
for i in sp.arange(6):
    diff[i] = name_integral(-(sp.pi)/2,(sp.pi)/2) - trapezoid(f,-(sp.pi)/2,(sp.pi)/2,n[i])
    diff[i] = abs(diff[i]) #returns absolute value of differences
    diff[i] = sp.log(diff[i]) #returns natural log of differences
    n_ln[i] = sp.log(n[i])
print 'The x-coordinates are:'
print n_ln
print 'The y-coordinates are:'
print diff
pl.plot(n_ln,diff)
pl.xlabel('ln(n)')
pl.ylabel('ln(Difference)')
pl.title('Natural Log of "n" vs. Natural Log of the Difference')
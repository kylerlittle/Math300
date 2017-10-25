# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 10:41:46 2016

@author: kylerlittle
"""

import pylab as pl
from math import factorial
def s(x,n):
    num = pl.zeros(n+1)
    denom = pl.zeros(n+1)
    result = pl.zeros(n+1)
    for i in pl.arange(0,n+1,1):
        num[i] = x**i
        denom[i] = factorial(i)
        result[i] = num[i]/denom[i]
        partial = pl.cumsum(result)
    pl.plot(pl.arange(0,n+1,1), partial, 'bo')
    pl.xlabel('n')
    pl.ylabel('s(x,n)')
    pl.title('Partial Sums Graph of s(x,n,)')
    pl.show()
    return partial
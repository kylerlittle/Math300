# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 10:40:30 2016

@author: kylerlittle
"""
import pylab as pl
def f(a,b):
    x = pl.arange(a,b,.01)
    pl.plot(x,pl.cos(x),'b')
    pl.plot(x,pl.sin(x),'y')
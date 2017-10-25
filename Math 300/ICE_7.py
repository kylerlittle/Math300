# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 10:51:21 2016

@author: kylerlittle
"""

import sympy as sp
sp.var('x')
sp.var('y')
z = 7
sp.solve(x+z,x)
#sp.solve(((x**3)-((2)*x**2)+(sp.pi*(y**2)-(2*(x+y)))),((x**2+y**2),[x,y])
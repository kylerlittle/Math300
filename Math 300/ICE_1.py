# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 10:58:23 2016

@author: kylerlittle
"""

import numpy as np
x=np.ones(5)
A = 4 * np.diag(x)
A[4,4]=-2
A[2,2]=np.cos((np.pi)/6)
A[3,3]=np.cos((np.pi)/6)
A[2,3]=-np.sin(np.pi/6)
A[3,2]=np.sin(np.pi/6)
A
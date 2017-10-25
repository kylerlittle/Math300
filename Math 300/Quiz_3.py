# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 10:52:02 2016

@author: kylerlittle
"""

import numpy as np
y = np.zeros((15,), dtype=np.int)
for i in np.arange(15):
    y[i] = (i+1)**2
print y
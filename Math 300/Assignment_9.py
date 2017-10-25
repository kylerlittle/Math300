# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 11:13:24 2016

@author: kylerlittle
"""
import numpy as np
name = str('kyler')
output = [] #output is an empty basic Python list, NOT array yet
for letter in name:
    number = ord(letter) - 96 #lowercase alphabet starts at 97 (a=97)
    output.append(number) #adds result to the empty list called 'output'
name = output
print name
x = np.asarray(name,dtype=float)
x = (x-13)/6
for i in np.arange(5):
    x[i] = x[i]/(2**i)
y = str('The coefficients of the kyler polynomial are')
print y
print x
def p(n):
    poly = (((((((x[4]*n)+x[3])*n)+x[2])*n)+x[1])*n)+x[0] #Horner's Method
    return poly
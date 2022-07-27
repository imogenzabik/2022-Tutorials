# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 13:39:05 2022

@author: imoge
"""
import numpy as np

def forward_diff(f,x,h):
    approx = (f(x+h)-f(x))/h
    return approx

def func_a(x):
    return x**3

x = np.array([-5,-3,-1,1,3,5])
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 22:02:40 2021

@author: Ghasemi
"""

def function (x):
    return((x**3)-(1-x)*5)
def bisection(a,b):
    cold=(a+b)/2
    f= function(cold)
    while abs(f)>=0.01:
        if function(cold)*function(a)<0:
            b=cold
        else:
            a=cold
        cnew=(a+b)/2 
        cold=cnew
        f=function(cold)
        print(cold)    
 
        
a=0
b=1
bisection(a,b)


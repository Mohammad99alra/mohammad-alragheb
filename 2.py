# -*- coding: utf-8 -*-
"""
Created on Thu May 23 20:19:48 2024

@author: FX-tec
"""

b = list (input("input binary number :"))
x = 0
for i in range (len(b)):
    digit = b.pop()
   if digit == '1' :
       
       x == x + pow(2, i)
       print("the decimal value of number " , x)
       
       
    
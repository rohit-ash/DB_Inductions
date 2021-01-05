# -*- coding: utf-8 -*-
"""
Created on Wed May 27 14:12:00 2020

@author: Rohit
"""


"fiZZ-bUZZ"

for i in range(1,101):
    if(i%3 == 0 and i%5 ==0):
        print ("FizzBuzz")
    elif(i%3 == 0):
        print("Fizz")
    elif (i%5==0):
        print("Buzz")
    else:
        print (i)

    
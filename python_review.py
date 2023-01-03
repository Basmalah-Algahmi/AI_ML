# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 14:16:43 2023

@author: BALGAHM1


"""


def ifStatement():
    a = 33
    b = 200
    if b > a:
      print("b is greater than a")
      
      
def whileLoop():
    a = 1
    b = 4
    while(a < b):
      print("a is ",a)
      a = a + 1
      
def forLoop():
    a=10
    for x in range(1, 5, 1):
      print(a)
      a =a +10
      
    fruits = {"Apple" , "Banana"}
    for x in fruits:
        print(x)
      
      

      
      
print("This is a python review")

ifStatement()
whileLoop()
forLoop()





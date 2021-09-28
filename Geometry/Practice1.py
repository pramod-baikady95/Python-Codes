# -*- coding: utf-8 -*-
"""
Created on Fri May  1 18:13:52 2020

@author: HP
"""

def foo(x):
    x += 1
    if x<20:
        print ('The value of X1: ',x)
        return foo(x)+1
    else:
        print ('The value of X2: ',x)
        return x
    
x = 10
print('The value of X3: ',foo(x))

#def change1(mylist):
#    mylist[0] = 2
#    print(mylist)
#    return
#
#def change2(mylist):
#    mylist = [1,2,3,4]
#    print(mylist)
#    return
#
#mylist = [10,20,30]
#change1(mylist)
#print(mylist)
#change2(mylist)
#print(mylist)

#import numpy as np
#x1 = np.arange(8)
#x2 = np.reshape(x1,(2,4))
#print(np.roll(x2,1,axis=0))
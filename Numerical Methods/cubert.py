# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 20:28:59 2020

@author: HP
"""

cube = float (input ("Enter the number to find it's cube root : "))
eps = 0.01
increment = 0.001
num_guess = 0
guess = float (input ("Enter the initial guess for the cube root : "))
while abs(guess**3 - cube) >= eps :
    guess += increment
    num_guess += 1
print("Number of Guess",num_guess)
if abs(guess**3 - cube) >= eps :
    print("Failed on cube root of",cube)
else:
    print(guess,"is the approximate cube root of",cube)

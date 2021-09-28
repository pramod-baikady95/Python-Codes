# -*- coding: utf-8 -*-
"""
Created on Sat May  2 16:10:53 2020

@author: HP
"""

import numpy as np
import math

""" Calculating the Area of triangle from the three sides """

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
        
class Triangle:
    
    def __init__(self, side1, side2, side3):
        self.a = side1
        self.b = side2
        self.c = side3
    
    def Tri_area(self):
        s = 0.5 * (self.a + self.b + self.c)
        area = math.sqrt(s * (s-self.a) * (s-self.b) * (s-self.c))
        return area
    

def side():
        side1 = math.sqrt((P1.x - P2.x)**2 + (P1.y - P2.y)**2 + (P1.z - P2.z)**2)
        side2 = math.sqrt((P2.x - P3.x)**2 + (P2.y - P3.y)**2 + (P2.z - P3.z)**2)
        side3 = math.sqrt((P1.x - P3.x)**2 + (P1.y - P3.y)**2 + (P1.z - P3.z)**2)
        
        print(side1)
        print(side2)
        print(side3)
        return side1, side2, side3


P1 = Point(0,0,0)
P2 = Point(3,0,0)
P3 = Point(0,4,0)
a, b, c = side()

T1 = Triangle(a, b, c)
T1.Tri_area()
print ('The area of the Triangle is : ' , T1.Tri_area())

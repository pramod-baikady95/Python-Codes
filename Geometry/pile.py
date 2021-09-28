# -*- coding: utf-8 -*-
"""
Created on Fri May  1 18:56:59 2020

@author: HP
"""

import numpy as np
import random

numberOfPiles = 100
maxIter = 1000000

piles = np.empty(numberOfPiles)
piles.fill(numberOfPiles)
totPiles = np.sum(piles)
numPiles = numberOfPiles
x=0
while (x < maxIter and piles.size >1):
    piles = piles[np.nonzero(piles)]
    for i in np.arange(piles.size):
        piles[i] -= 1
        num = np.random.randint(piles.size)
        piles[num] +=1
    numPiles = piles.size
    x +=1
print(" The number of piles remaining are: ", numPiles)
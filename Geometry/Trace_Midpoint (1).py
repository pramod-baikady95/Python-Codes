#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[31]:


Base_X = np.arange(0,100)
Base_Y = np.zeros(len(Base_X))
Top_X = np.zeros(len(Base_X))
Top_Y = np.zeros(len(Base_X))
MP_X = np.zeros(len(Base_X))
MP_Y = np.zeros(len(Base_X))
Length = max(Base_X)

for i in (Base_X):
    Top_Y[i] = np.sqrt(Length**2 - Base_X[i]**2)
    MP_X[i] = (Base_X[i]+Top_X[i])/2
    MP_Y[i] = (Base_Y[i]+Top_Y[i])/2
    
plt.plot(MP_X,MP_Y)
plt.axis("square")
plt.title("Tracing the Center of the Sliding Ladder")
plt.xlabel("Ladder Mid Point X co-ordinate ")
plt.ylabel("Ladder Mid Point Y co-ordinate ")
plt.savefig("Curve_Trace.png")
plt.show()


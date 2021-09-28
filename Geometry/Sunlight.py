#!/usr/bin/env python
# coding: utf-8

# In[11]:


# Function to calculate the total length of the surface exposed to the source light
# Assumption is made for two or more rectangular buildings and Source light is always higher than the building

def exposed_surface(BP,SP):
    
    # Hor_dist calculates the horizontal distance between the two adjacent buildings
    # hyp calculates the hypotenuse distance between the two adjacent buildings 
    # Vert_dist is calculated using the Pythogorous theorem apllied for Hor_dist and hyp
    # incl is the absolute tangential slope value between the source and right top corner of the building 
    # shadow_slope calculates the additional exposed surface length 
    # Surf_length calculates the total length of the surface exposed to the surface light
    
    
    # initializing
    
    Hor_dist = [0]*(len(BP)-1)
    Vert_dist = [0]*(len(BP)-1)
    hyp = [0]*(len(BP)-1)
    shadow_slope = [0]*(len(BP)-1)
    incl = [0]*(len(BP)-1)
    Surf_length = 0
    
    # Calculating the vertical length of the first building
    Surf_length = ((BP[0][0][1]- BP[0][1][1])**2 )**(1/2)
    
    # Calculating the total horizontal length of all the building exposed to source light
    for i in range(len(BP)):
        Surf_length += ((BP[i][1][0]- BP[i][2][0])**2)**(1/2)
            
    # Calculation for finding the additional exposed surface length
    for i in range(len(BP)-1):
        if (BP[i+1][1][1] > BP[i][2][1]):
            hyp[i] = ((BP[i][2][0] - BP[i+1][1][0])**2 + (BP[i][2][1] - BP[i+1][1][1])**2 )**(1/2)
            Hor_dist[i] = ((BP[i][2][0] - BP[i+1][1][0])**2)**(1/2)
            Vert_dist[i] = ((hyp[i])**2 - (Hor_dist[i])**2)**(1/2)
            incl[i] = ((((SP[1] - BP[i][2][1]))/((SP[0] - BP[i][2][0])))**2)**(1/2)
            shadow_slope[i] = incl[i]*Hor_dist[i]
            Surf_length += (Vert_dist[i]+ shadow_slope[i])
        
        
    return Surf_length


# In[15]:


# Defining the Building Coordinates and the location of Source light
# Building Coordinates are defined in the following order
# left bottom corner, left top corner, right top corner and right bottom corner 

Building_points = [[[0,0],[0,7.5],[5,7.5],[5,0]],[[8,0],[8,12],[15,12],[15,0]]]
Source_Point = [-5,15]

exp_surf = exposed_surface(Building_points,Source_Point)
print('===========================================================================')
print('The total length of the surface exposed to the source light is %g units' %(exp_surf))
print('===========================================================================')


# In[ ]:





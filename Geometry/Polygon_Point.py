#!/usr/bin/env python
# coding: utf-8

# In[21]:


# Function to calculate the area of the Polygon using Shoelace method along with the Centroid 

def Polygon_Area(vp):
    
    # Initializing
    CG = [0,0]
    n = len(vp)
    Poly_Area = 0
    
    # Vertices
    for i in range(len(vp)):
        
        x0 = vp[i][0]
        y0 = vp[i][1]
        
        x1 = vp[(i+1) % n][0]
        y1 = vp[(i+1) % n][1]
        
        # Calculating the Area using Shoelace formula
        A = (x0*y1) - (x1*y0)
        Poly_Area += A
        
        # Calculating the Coordinates of centroid of Polygon
        CG[0] += (x0 + x1)*A
        CG[1] += (y0 + y1)*A
        
    Poly_Area *= 0.5
    CG[0] = (CG[0])/(6*Poly_Area)
    CG[1] = (CG[1])/(6*Poly_Area)
    
    return Poly_Area


# In[22]:


# Nearest Points

def nearest_point(vp,tp):
    
    # initializing 
    Length = [0]*len(vp)
    print('')
    
    # calculating the distance between the test point and the vertices of the polygon 
    for i in range(len(vp)):
        Length[i] = ((tp[0]-vp[i][0])**2 + (tp[1]-vp[i][1])**2)**(1/2)
        
    # finding the two nearest points w.r.t the Test Point
    
    # finding the index to insert the test point to the existing vertices of polygon
    
    closest_length = list(sorted(Length))
    
    for i in range(len(vp)):
        if (Length[i] == closest_length[0]):
            np1 = i
            print('The Point %g is the first closest point' %(i))
            break  
    
    for i in range(len(vp)):
        if (Length[i] == closest_length[1]): 
            np2 = i
            print('The Point %g is the second closest point' %(i))
            break
    if np1>np2:
        near_point = np1
    else:
        near_point = np2
    
    return near_point
    


# In[23]:


# Function to check if the Point lies within the polygon by comparing the polygon area
# Call the Polygon Area function and Nearest Point function
# if the Area of the given polygon is lesser than the Area of the polygon formed adding the test point vertex
# the test point falls outside the polygon, else it falls within the polygon

def is_point_inside(vp,tp):
    print('=====================================================')
    Poly_Area1 = Polygon_Area(vertex_points)
    print('The Area of the given Polygon is %g square unit' %(Poly_Area1))
    print('=====================================================')

    insert_point = nearest_point(vp,tp)
    vertex_points.insert(insert_point, tp)

    Poly_Area2 = Polygon_Area(vertex_points)
    print('======================================================================')
    print('The Area of the Polygon with test point vertex is %g square unit' %(Poly_Area2))
    print('======================================================================')

    print('')
    if Poly_Area1 < Poly_Area2:
        print('The test point falls Outside the given Polygon')
        print('')
        return False
    else:
        print('The test point falls inside the given Polygon')
        print('')
        return True
    



# In[24]:


# Driver code

# Coordinates of the vertices of Polygon and the test point

vertex_points = [[0,0],[5,0],[5,5],[0,5]]
test_point = [4,6]

test = is_point_inside(vertex_points,test_point)

print('=====================================================')
print(test)
print('=====================================================')       


# In[ ]:





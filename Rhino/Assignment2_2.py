import rhinoscriptsyntax as rs
import math
import random as rnd

#Create a point grid
Xaxis = rs.GetInteger('X')
Yaxis = rs.GetInteger('Y')

#Create empty list called ptList
ptList = []

#Loop and append in pt List
for i in range(Xaxis):
    for j in range(Yaxis):
        x = i *(i+5)
        y = j *(j+5)
        z = 0
        rs.AddPoint(x,y,z)
        ptList.append((x,y,z))
#for i in range(len(ptList)):
#    rs.AddTextDot(i, ptList[i])
#print ptList


#How many random points
aN = rs.GetInteger('# RANDOM POINTS')

#Attractor (x & y) 
axpts = []
aypts = []

#Random points list
aList = []

#Append random points 
for m in range(aN):
    print m
    axpts.append(rnd.randint(0,x))
    aypts.append(rnd.randint(0,y))
    aList.append(rs.AddPoint(axpts[m],aypts[m],0))
    
    
baseObj = rs.GetObject('Base Object',rs.filter.curve)

#Get centroid of the curve "Base Object"
cen = rs.CurveAreaCentroid(baseObj)

#Copy curve "star"
for pt in range(len(ptList)):
    translation = ((ptList[pt][0]-cen[0][0]),(ptList[pt][1]-cen[0][1]),(ptList[pt][2]-cen[0][2]))
    rs.CopyObject(baseObj,translation)
    
#Lines from randon points to grid points
    for a in range(len(aList)):
        rs.AddCurve((ptList[pt], aList[a]),1)





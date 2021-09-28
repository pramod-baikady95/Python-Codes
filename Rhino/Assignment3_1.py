#assignment3.1
#using dictionary in assignment2.2's pattern

import rhinoscriptsyntax as rs

ptList = []
ptDict = {}
crvList = []

mSize = 12

#generate matrix
for i in range (mSize):
    for j in range (mSize):
        x = i*(j+i)+5
        y = j*(i+j)+5
        z = 0
        pts = rs.AddPoint(x,y,z)
        ptDict[(i,j)] = (x,y,z)#module shape of dict

#generate geometry
for i in range (mSize):
    for j in range (mSize):
        if i>0 and j>0:
           #add closed 3degree crvs and scale it:
           bigClosedCrv = rs.AddCurve((ptDict[(i,j)],ptDict[(i-1,j)],
           ptDict[(i-1,j-1)],ptDict[(i,j-1)],ptDict[(i,j)]))
           centroid = rs.AddPoint(rs.CurveAreaCentroid(bigClosedCrv)[0])
           smClosedCrv = rs.CopyObject(bigClosedCrv) 
           rs.ScaleObject(bigClosedCrv, centroid, (1.5,1.5,1.5))
           rs.ScaleObject(smClosedCrv,centroid,(.5,.5,.5))               
           crvList.append(bigClosedCrv) 
              
#add colors               
for k in range (len(crvList)):
    if k%3 == 0:
        rs.ObjectColor((crvList[k]), ((255,128,0)))
    else:
        rs.ObjectColor((crvList[k]), (0,255,255))

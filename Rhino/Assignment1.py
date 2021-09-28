import rhinoscriptsyntax as rs
import math

#Create the Origin and End Points which forms the first line
originPt = (0,0,0)
point1 = (0,10,0)
line1 = rs.AddLine(originPt,point1)

#Copy and translate the line1 object to create line2 and line3 0bjects at 5 unit
# offset from X&Y axes
line2 = rs.CopyObject(line1, (5,5,0))
line3 = rs.CopyObject(line1, (-5,5,0))

# Creating the lines with Scaling and Rotation
# New lines are created from origin to the start points of line2 and line3
scaleFactor = math.cos(math.pi/4)
line4 = rs.ScaleObject( line1, originPt, (scaleFactor,scaleFactor,0), True )
line4 = rs.RotateObjects( line4, originPt, -45.0, None, False )
line5 = rs.ScaleObject( line1, originPt, (scaleFactor,scaleFactor,0), True )
line5 = rs.RotateObjects( line5, originPt, 45.0, None, False )

#Copy and translate the line4 and line5 object to create line6 and line7 objects 
#at the end of the line1
line6 = rs.CopyObject(line5, point1)
line7 = rs.CopyObject(line4, point1)

#Creating reference points and Rotating line6 and Line7 to complete the base of 
#the 2D Pattern
point2 = (-5,15,0)
point3 = rs.PointAdd(point2, (10,0,0))
line8 = rs.RotateObjects( line6, point2, 90.0, None, True )
line9 = rs.RotateObjects( line7, point3, -90.0, None, True )

#Select the Objects for patterning
baseObj = rs.GetObjects("Select all the objescts for Linear patterning")
baseCopy1 = rs.CopyObject(baseObj, rs.PointAdd(originPt,(0,20,0)))
baseCopy2 = rs.CopyObject(baseObj, rs.PointAdd(originPt,(0,40,0)))
baseCopy3 = rs.CopyObject(baseObj, rs.PointAdd(originPt,(0,60,0)))
baseCopy4 = rs.CopyObject(baseObj, rs.PointAdd(originPt,(0,80,0)))
baseCopy5 = rs.CopyObject(baseObj, rs.PointAdd(originPt,(0,100,0)))
baseCopy6 = rs.CopyObject(baseObj, rs.PointAdd(originPt,(0,120,0)))

baseObj2 = rs.GetObjects("Select all the objescts for Circular patterning")
baseCopy7 = rs.RotateObjects( baseObj2, originPt, 45.0, None, True )
baseCopy8 = rs.RotateObjects( baseObj2, originPt, 90.0, None, True )
baseCopy9 = rs.RotateObjects( baseObj2, originPt, 135.0, None, True )
baseCopy10 = rs.RotateObjects( baseObj2, originPt, 180.0, None, True )
baseCopy11 = rs.RotateObjects( baseObj2, originPt, 225.0, None, True )
baseCopy12 = rs.RotateObjects( baseObj2, originPt, 270.0, None, True )
baseCopy13 = rs.RotateObjects( baseObj2, originPt, 315.0, None, True )

#Generating Concentric Circles
circle1 = rs.AddCircle(originPt,20)
circle2 = rs.AddCircle(originPt,30)
circle3 = rs.AddCircle(originPt,40)
circle4 = rs.AddCircle(originPt,50)
circle5 = rs.AddCircle(originPt,60)
circle6 = rs.AddCircle(originPt,70)
circle7 = rs.AddCircle(originPt,80)
circle8 = rs.AddCircle(originPt,90)
circle9 = rs.AddCircle(originPt,100)
circle10 = rs.AddCircle(originPt,110)
circle11 = rs.AddCircle(originPt,120)
circle13 = rs.AddCircle(originPt,130)
circle14 = rs.AddCircle(originPt,140)

#Generating Circles to form flower petal pattern
circle15 = rs.AddCircle((100,0,0),100)
circle16 = rs.AddCircle((100*scaleFactor,100*scaleFactor,0),100)
circle17 = rs.AddCircle((0,100,0),100)
circle18 = rs.AddCircle((-100*scaleFactor,100*scaleFactor,0),100)
circle19 = rs.AddCircle((-100,0,0),100)
circle20 = rs.AddCircle((-100*scaleFactor,-100*scaleFactor,0),100)
circle21 = rs.AddCircle((0,-100,0),100)
circle22 = rs.AddCircle((100*scaleFactor,-100*scaleFactor,0),100)
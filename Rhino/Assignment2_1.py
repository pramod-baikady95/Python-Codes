
#BONE STRUCTURE THREE
import rhinoscriptsyntax as rs
import random as rnd

#input a point
ptGUID = rs.GetObject('select a point', rs.filter.point)

#randomly generate circle radius
radius = rnd.randint(12,25)
print radius

#draw a circle using point as origin
circle = rs.AddCircle(ptGUID, radius)
circle10 = rs.AddCircle(ptGUID, radius/4)
rs.HideObject(circle)

#divide circle - save points in a list
pts = rs.DivideCurve(circle, 8, False, True)

#label points
#rs.AddTextDot('pts[0]', pts[0])
#rs.AddTextDot('pts[1]', pts[1])
#rs.AddTextDot('pts[2]', pts[2])
#rs.AddTextDot('pts[3]', pts[3])
#rs.AddTextDot('pts[4]', pts[4])
#rs.AddTextDot('pts[5]', pts[5])
#rs.AddTextDot('pts[6]', pts[6])
#rs.AddTextDot('pts[7]', pts[7])
#rs.AddTextDot('pts[8]', pts[8])

########CREATE GEOMETRY#########
#Psuedo Code
#draw curve (ptGUID, pts[0], pts[1], ptGUID)
c1 = rs.AddCurve((ptGUID, pts[0], pts[1], ptGUID))

#draw curve (ptGUID, pts[1], pts[2], ptGUID)
c2 = rs.AddCurve((ptGUID, pts[1], pts[2], ptGUID))

#draw curve (ptGUID, pts[2], pts[3], ptGUID)
c3 = rs.AddCurve((ptGUID, pts[2], pts[3], ptGUID))

#draw curve (ptGUID, pts[3], pts[4], ptGUID)
c4 = rs.AddCurve((ptGUID, pts[3], pts[4], ptGUID))

#draw curve (ptGUID, pts[4], pts[5], ptGUID)
c5 = rs.AddCurve((ptGUID, pts[4], pts[5], ptGUID))

#draw curve (ptGUID, pts[5], pts[6], ptGUID)
c6 = rs.AddCurve((ptGUID, pts[5], pts[6], ptGUID))

#draw curve (ptGUID, pts[6], pts[7], ptGUID)
c7 = rs.AddCurve((ptGUID, pts[6], pts[7], ptGUID))

#draw curve (ptGUID, pts[7], pts[0], ptGUID)
c8 = rs.AddCurve((ptGUID, pts[7], pts[0], ptGUID))

p1 = rs.AddPoint(rs.CurveAreaCentroid(c1)[0])
p2 = rs.AddPoint(rs.CurveAreaCentroid(c2)[0])
p3 = rs.AddPoint(rs.CurveAreaCentroid(c3)[0])
p4 = rs.AddPoint(rs.CurveAreaCentroid(c4)[0])
p5 = rs.AddPoint(rs.CurveAreaCentroid(c5)[0])
p6 = rs.AddPoint(rs.CurveAreaCentroid(c6)[0])
p7 = rs.AddPoint(rs.CurveAreaCentroid(c7)[0])
p8 = rs.AddPoint(rs.CurveAreaCentroid(c8)[0])

circle1 = rs.AddCircle(p1, radius/10)
circle2 = rs.AddCircle(p2, radius/10)
circle3 = rs.AddCircle(p3, radius/10)
circle4 = rs.AddCircle(p4, radius/10)
circle5 = rs.AddCircle(p5, radius/10)
circle6 = rs.AddCircle(p6, radius/10)
circle7 = rs.AddCircle(p7, radius/10)
circle8 = rs.AddCircle(p8, radius/10)

line1 = rs.AddLine(ptGUID,p1)
line2 = rs.AddLine(ptGUID,p2)
line3 = rs.AddLine(ptGUID,p3)
line4 = rs.AddLine(ptGUID,p4)
line5 = rs.AddLine(ptGUID,p5)
line6 = rs.AddLine(ptGUID,p6)
line7 = rs.AddLine(ptGUID,p7)
line8 = rs.AddLine(ptGUID,p8)

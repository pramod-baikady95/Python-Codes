#BONE STRUCTURES ONE
import rhinoscriptsyntax as rs

#input rectangle
crvGUID = rs.GetObject('select a rectangle', rs.filter.curve)
rs.HideObject(crvGUID)

#find edit points
pts = rs.CurveEditPoints(crvGUID)

#find centroid
centroid = rs.CurveAreaCentroid(crvGUID)[0]

#create points in rhinospace
#rs.AddPoints(pts)
#rs.AddPoint(centroid)

#label points
#rs.AddTextDot('pts[0]', pts[0])
#rs.AddTextDot('pts[1]', pts[1])
#rs.AddTextDot('pts[2]', pts[2])
#rs.AddTextDot('pts[3]', pts[3])
#rs.AddTextDot('centroid', centroid)

########CREATE GEOMETRY#########
#PSUEDO CODE

#draw line from pts[0], centroid, pts[1]
rs.AddCurve((pts[0], centroid, pts[1]))

#draw line from pts[1], centroid, pts[2]
rs.AddCurve((pts[1], centroid, pts[2]))

#draw line from pts[2], centroid, pts[3]
rs.AddCurve((pts[2], centroid, pts[3]))

#draw line from pts[3], centroid, pts[0]
rs.AddCurve((pts[3], centroid, pts[0]))

#construct a closed curve from corner points
curve = rs.AddCurve(pts)

#scale curve using centroid as origin
rs.ScaleObject(curve, centroid, (.5,.5,.5))

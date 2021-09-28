#Assignment 5
#Modular Tower
#import modules
import rhinoscriptsyntax as rs
import random as rnd

def SurfacePoints(STRSRF, INTU, INTV):
    #create empty dictionary
    ptMTX = {}
    srfNorm01 = {}
    srfNorm02 = {}
    
    #find domain of surface
    Udomain = rs.SurfaceDomain(STRSRF,0)
    Vdomain = rs.SurfaceDomain(STRSRF,1)
    
    #calculate step values
    stepU = (Udomain[1] - Udomain[0])/INTU
    stepV = (Vdomain[1] - Vdomain[0])/INTV
    
    #find list of expanding step values
    expStep = DivideExponentially((Udomain[1] - Udomain[0]), INTU)
#    print expStep
    
    #PLOT POINTS ON SURFACE
    for i in range(INTU+1):
        for j in range(INTV+1):
            #define u and v in terms of step values and i and j
            #u = Udomain[0] + stepU * i #+(rnd.random())
            u = expStep[i]
            v = Vdomain[0] + stepV * j #+(rnd.random())
            #v = expStep[j]
            
            #evaluate surface
            point = rs.EvaluateSurface(STRSRF, u, v)
            #rs.AddPoint(point)
            ptMTX[(i,j)] = point
            
            #find surface normal(vector) at parameter
            vecNorm = rs.SurfaceNormal(STRSRF, (u, v))
            #print vecNorm
            #unitize vector for scaling
            vecNorm = rs.VectorUnitize(vecNorm)
            #make scale a factor of the distance from the cPlane
            plane = rs.WorldXYPlane()
            distance = rs.DistanceToPlane(plane, point)
            #print 1-distance/20
            #scale vector
#            vecNorm = rs.VectorScale(vecNorm, 1-distance/20)#.5
            vecNorm = rs.VectorScale(vecNorm, 1)
            #SAVE FIRST POSITION OF vecNorm IN DICTIONARY srfNorm01
            srfNorm01[(i,j)] = rs.PointAdd(vecNorm,point)
            #unitize and scale vector 
            vecNorm = rs.VectorUnitize(vecNorm)
            vecNorm = rs.VectorScale(vecNorm, 3)
            vecNorm = rs.PointAdd(vecNorm,point)
            #SAVE SECOND POSITION OF vecNorm IN DICTIONARY srfNorm02
            srfNorm02[(i,j)] = vecNorm
            
    #call function to generate geometry - sending dictionaries of points
    GenerateGeometry(ptMTX, srfNorm02, srfNorm01, INTU, INTV) 
                
def GenerateGeometry(ptMTX, srfNorm02, srfNorm01, INTU, INTV):
    #LOOP TO CREATE GEOMETRY
    for i in range(INTU+1):
        for j in range(INTV+1):
            if i > 0 and j > 0:
                ####  CREATE firstCrv CURVE  ####
                #find mid point to use as centroid
                centroid = MidPt(ptMTX[(i,j)], ptMTX[(i-1,j-1)])
                #construct a point at the middle of the left edge
                middlePt = MidPt(ptMTX[(i-1,j-1)], ptMTX[(i-1,j)])
                #rs.AddPoint(centroid)
                curves = []
                #straight-line segments
                curves.append(rs.AddCurve((ptMTX[(i,j)], middlePt, ptMTX[(i,j-1)]),1))
                #curved segment
                curves.append(rs.AddCurve((ptMTX[(i,j-1)], centroid, ptMTX[(i,j)]),3))
                
                #join curves deleting original curves
                firstCrv = rs.JoinCurves(curves, True)
                #find start point
                #rs.AddPoint(rs.CurveStartPoint(outerCrv))
                
                ####  CREATE secondCrv CURVE  ####
                #construct a point at the middle of the left edge
                middlePt = MidPt(srfNorm01[(i-1,j-1)], srfNorm01[(i-1,j)])
                #rs.AddPoint(centroid)
                curves = []
                #straight-line segments
                secondCrv = rs.AddCurve((srfNorm01[(i,j)], middlePt, srfNorm01[(i,j-1)], srfNorm01[(i,j)]),1)
                
                middlePt = MidPt(srfNorm02[(i-1,j-1)], srfNorm02[(i-1,j)])

                #find centroid for inner curve
                centroid = MidPt(srfNorm02[(i,j)], srfNorm02[(i-1,j-1)])
                thirdCrv = rs.AddCurve((srfNorm02[(i,j-1)], srfNorm02[(i,j)], middlePt, srfNorm02[(i,j-1)]),3)

                plane = rs.WorldXYPlane()
                distance = rs.DistanceToPlane(plane, ptMTX[(i,j)])
                #print 1-distance/20
                #scale inner curve with centroid
                rs.ScaleObject(thirdCrv, centroid, (1-distance/40,1-distance/40,1-distance/40))#(.4,.4,.4)
                #loft curves to create surfaces
                module = rs.AddLoftSrf((firstCrv, secondCrv, thirdCrv), None, None,2,0)
             
                #add color to module
                red = 255/INTU*j
                if red < 0: red = 0
                if red > 255: red = 255
                green = 255-(255/INTU)*j
                blue = 255-(255/INTU)*j
                
                
                rs.ObjectColor(module,(red, green, blue))
                mat_index = rs.AddMaterialToObject(module)
                rs.MaterialColor(mat_index, (red, green, blue))
                
    
def MidPt(PT01, PT02):
    
    #clear all data being held in point variable
    point = None
    #calculate mid-point position from input point data
    point = [(PT01[0] + PT02[0]) / 2,(PT01[1] + PT02[1]) / 2,
    (PT01[2] + PT02[2]) / 2,]
    #return mid-point to main() function where MidPt() function was called
    return point
                
def DivideExponentially(maxLength, Divisions):
    #set-up lists
    point = []
    yVal = []
    
    #create point where x is .72 of Vdomain and y and z are 0 (point[0])
    pt = ([(maxLength*.82), 0, 0])
    #rs.AddPoint(pt)
    point.append(pt)
    
    #create point where x and y are .12 of model curve length and z is 0 (point[1])
    pt = ([(maxLength*.25), (maxLength*.25), 0])
    #rs.AddPoint(pt)
    point.append(pt)
    
    #create point where y is model curve length and x and z are 0 (point[2])
    pt = ([0, maxLength, 0])
    #rs.AddPoint(pt)
    point.append(pt)
    
    #draw a curve between the three points (GRAPHcrvGUID)
    GRAPHcrvGUID = rs.AddCurve(point)
    
    #divide (GRAPHcrvGUID)
    GRAPHpoints = rs.DivideCurve(GRAPHcrvGUID, Divisions, False, True)
    
    #delete curve
    rs.DeleteObject(GRAPHcrvGUID)
    
    #collect y values in a list
    for i in range(len(GRAPHpoints)):
        yVal.append(GRAPHpoints[i][1])
        
    return yVal
    
def main():
    #collect data
    #strSRF = rs.GetObject('select surface', rs.filter.surface)
    strSRFs = rs.GetObjects('select surfaces', rs.filter.surface)
    intU = rs.GetInteger('how many U intervals?', 8)
    intV = rs.GetInteger('how many V intervals?', 8)
    
    #call function with multiple surfaces
    rs.EnableRedraw(False)
    for strSRF in strSRFs:
        rs.HideObject(strSRF)
        #call function
        SurfacePoints(strSRF, intU, intV)
    rs.EnableRedraw(True)
    
main()

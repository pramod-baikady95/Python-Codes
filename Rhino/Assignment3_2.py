#ANIMATION EXAMPLE
import rhinoscriptsyntax as rs
import random as rnd

#input the number of frames you want to produce
num_of_frames = rs.GetInteger('Number of Frames to Output?', 10)
    
#loop through the number of frames creating the animation
for frame in range(num_of_frames):
    
#######________YOUR CODE GOES (INDENTED) BELOW THIS LINE________########
    #'frame' is your iteration variable - its simply counting from 0 to the maximum
    #number of frames that you input (num_of_frames)
    #use the 'frame' variable in your code to change something - to produce the 
    #animation.
    
    #Create and position object to animate
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
               #centroid = rs.AddPoint(rs.CurveAreaCentroid(bigClosedCrv)[0])
               centroid = rs.CurveAreaCentroid(bigClosedCrv)[0]
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
    
    #Set variable to animate and amplify/accelerate movement/animation as desired
    rs.RotateObject(crvList, (0,0,0),30*frame,None,False)
    
#######________YOUR CODE GOES (INDENTED) ABOVE THIS LINE________########
    
    #Specify local folder to output frames -- you will need to change this to a
    #correct path on your computer
    render_folder = "C:\\Users\\pramo\\Desktop\\Animation\\"
    
    
    def render_step(render_folder, sequence_num):
        #Captures screenshots of the scene frame
        file_name = str(int(sequence_num)).zfill(5)
        file_path = " " + render_folder + file_name + ".png"
        rs.Command("_-ViewCaptureToFile" + file_path + " _Enter")
    
    #Call function to render frame
    render_step(render_folder, frame)
    
    #Clear canvas for the next frame -- 
    #YOU HAVE TO DELETE ALL THE OBJECTS YOU ARE RENDERING
    #This could also be optional if you want to overlay the frames of your animation
    #If you're deleteing a single object use rs.DeleteObject()
    #If you're deleteing a list of objects use rs.DeleteObjects()
    rs.DeleteObjects(crvList)
    
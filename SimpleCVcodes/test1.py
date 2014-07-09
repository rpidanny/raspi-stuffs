import os, sys, pickle
from SimpleCV import Camera, Display , DrawingLayer , Color
#from SimpleCV import *
from time import sleep
from turtle import *


def halfsies(left,right): 
    result = left
    # crop the right image to be just the right side.
    crop   = right.crop(right.width/2.0,0,right.width/2.0,right.height)
    # now paste the crop on the left image.
    result = result.blit(crop,(left.width/2,0))
    # return the results.
    return result

myCamera = Camera()
#myCamera.live()
myDisplay = Display(resolution=(640, 480))

size =(myCamera.getImage().size())
center = (size[0]/2,size[1]/2)

redcircle = DrawingLayer((640, 480))
#redcircle.circle(((blobs[-1].minRectX()),40), 2, color=Color.RED)
while not myDisplay.isDone():
    #tmp=myCamera.getImage()
    img = myCamera.getImage().crop(0,220,640,80)
    
    output = img.binarize(40).invert()
    #output = img.binarize(80)
    #output.morphOpen()
    #output.erode(10)
    #output.dilate(20)
    #output.morphOpen()
    blobs = output.findBlobs()

    if(blobs is not None):
        blobs=blobs.sortArea()
        center=(int(blobs[-1].minRectX()),int(blobs[-1].minRectY()))
        if int(blobs[-1].minRectX())>330:
            print "left"
        if int(blobs[-1].minRectX())<310:
            print "right"


    output.dl().circle(center,2,Color.RED,width=2)
    output.dl().circle(center,15,Color.GREEN,width=6)



    #print int(center[-1].minRectX())   
    #blobs[-1].hullImage().show()
    #if float(blobs[-1].minRectX())<320.0:
    #    print "left"
    #else:
    #   print "right"
    #redcircle.circle((pos,40), 2, color=Color.RED)
    #output.addDrawingLayer(redcircle)
    #output.applyLayers()
    #print blobs[-1].hull()
    #points = blobs[-1].hull()
    #output.dl().polygon(points, filled=True, color=Color.RED)
    #blobs[-2].draw(Color.PUCE,width=-1,alpha=128)
    #result = halfsies(img,output)


    
    #tmp.dl().circle(center,2,Color.RED,width=2)
    #tmp.dl().circle(center,15,Color.GREEN,width=6)
    #tmp.show()

    output.show()
    sleep(.1)

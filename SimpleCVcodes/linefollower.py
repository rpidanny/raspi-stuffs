import os, sys, pickle
from SimpleCV import Camera, Display , DrawingLayer , Color
from time import sleep
from turtle import *
import smbus
import time


bus = smbus.SMBus(1)
address = 0x04

def writeNumber(value):
    bus.write_byte(address, value)
    return -1

def halfsies(left,right): 
    result = left
    crop   = right.crop(right.width/2.0,0,right.width/2.0,right.height)
    result = result.blit(crop,(left.width/2,0))
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
    img = myCamera.getImage().crop(40,220,560,80)
    
    output = img.binarize(60).invert()
    #output = img.binarize(70)
    #output.morphOpen()
    #output.erode(10)
    #output.dilate(20)
    #output.morphOpen()
    blobs = output.findBlobs()

    if(blobs is not None):
        blobs=blobs.sortArea()
        center=(int(blobs[-1].minRectX()),int(blobs[-1].minRectY()))
        if (int(blobs[-1].minRectX())<330 and int(blobs[-1].minRectX())>310):
            #print "Forward"
            writeNumber(1)
        elif int(blobs[-1].minRectX())>330:
            #print "left"
            writeNumber(2)
        elif int(blobs[-1].minRectX())<310:
            #print "right"
            writeNumber(3)
    else:
        #print "Stop"
        writeNumber(4)
            


    output.dl().circle(center,2,Color.RED,width=2)
    output.dl().circle(center,15,Color.GREEN,width=6)

    output.show()
    sleep(.1)

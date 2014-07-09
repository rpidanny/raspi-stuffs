from SimpleCV import JpegStreamCamera
from SimpleCV import Camera, Display
from time import sleep
cam= JpegStreamCamera("http://192.168.1.10:8070/")

myDisplay = Display(resolution=(640, 480))

while not myDisplay.isDone():
     img=cam.getImage()
     img.show()
     sleep(.1)

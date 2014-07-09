from SimpleCV import JpegStreamCamera
from SimpleCV import Camera, Display
from time import sleep
cam= JpegStreamCamera("http://192.168.1.4:8083/videofeed")
cam1= JpegStreamCamera("http://192.168.1.7:8070/videofeed")
myDisplay = Display(resolution=(640, 960))
#myDisplay1 = Display(resolution=(640, 480))
while not myDisplay.isDone():
     img=cam.getImage()
     img1=cam1.getImage()
     img.sideBySide(img1).show()
     sleep(.1)

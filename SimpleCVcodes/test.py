from SimpleCV import Camera, Display
from time import sleep
myCamera = Camera(prop_set={'width': 640, 'height': 480})
myDisplay = Display(resolution=(640, 480))
while not myDisplay.isDone():
 img = myCamera.getImage()
 img.show()
 sleep(.1)
myCamera.release()
del myCamera

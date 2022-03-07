from picamera import PiCamera
from time import sleep

def initialise_camera():
    camera = PiCamera()
    return camera
 
def get_and_create_image(camera):
    camera.start_preview()
    sleep(3)
    camera.capture('image.jpg')
    camera.stop_preview()
    camera.close()
    

def take_a_picture():
    camera = initialise_camera()
    get_and_create_image(camera)

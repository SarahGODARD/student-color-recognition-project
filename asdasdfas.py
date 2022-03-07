from picamera import PiCamera
from time import sleep

def initialise_camera():
    camera = PiCamera()
    return camera
 
def get_and_create_image(camera):
    camera.start_preview()
    camera.capture('image.jpg')

if __name__ == "__main__":
        camera = initialise_camera()
        get_and_create_image(camera)

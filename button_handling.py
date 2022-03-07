import RPi.GPIO as GPIO

def initialise_rgpio():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.IN)
    GPIO.setup(17, GPIO.IN)
    GPIO.setup(27, GPIO.IN)
    GPIO.setup(22, GPIO.IN)
    
def event_callback(channel):
    if GPIO.input(17):
        print("R", GPIO.input(17))
    if GPIO.input(18):
        print("G", GPIO.input(18))
    if GPIO.input(22):
        print("B", GPIO.input(22))
    if GPIO.input(27):
        print("A", GPIO.input(27))
        
def read_rgpio():
    GPIO.add_event_detect(17, GPIO.RISING, callback=event_callback, bouncetime=300)
    GPIO.add_event_detect(18, GPIO.RISING, callback=event_callback, bouncetime=300)
    GPIO.add_event_detect(22, GPIO.RISING, callback=event_callback, bouncetime=300)
    GPIO.add_event_detect(27, GPIO.RISING, callback=event_callback, bouncetime=300)
    
if __name__ == "__main__":
    print("youhou");
    initialise_rgpio();
    read_rgpio()
    print("end");
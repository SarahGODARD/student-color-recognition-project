import RPi.GPIO as GPIO
import subprocess
from getCamera import take_a_picture
from asdsadsadsa import initServo, changeAngle

i = 1

def initialise_rgpio():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(18, GPIO.IN)
    GPIO.setup(17, GPIO.IN)
    GPIO.setup(27, GPIO.IN)
    GPIO.setup(22, GPIO.IN)
    GPIO.setup(22, GPIO.IN)
    GPIO.setup(23, GPIO.OUT)  #busy
    GPIO.setup(24, GPIO.OUT)  #idle
    
def led_busy():
    GPIO.output(23, 1)
    GPIO.output(24, 0)
    
def led_idle():
    GPIO.output(23, 0)
    GPIO.output(24, 1)
    
def led_off():
    GPIO.output(23, 0)
    GPIO.output(24, 0)
    
def call_cpp():
    args = ("./a.out")
    popen = subprocess.Popen(args, stdout=subprocess.PIPE)
    popen.wait()
    output = popen.stdout.read()
    print(output)
    initServo()
    changeAngle(2, 30)
    

def event_callback(channel):
    global i
    if GPIO.input(17)and i==1:
        i+=1
        led_busy()
        print("find green color", GPIO.input(17))  #second
        print(i)
        take_a_picture()
        call_cpp()
    if GPIO.input(18):
        i=1                   
        print("reset", GPIO.input(18))  #first button
        print(i)
        led_off()
    if GPIO.input(22)and i==1:
        i+=1
        print("find red color", GPIO.input(22))
        print(i)
        led_busy()
        take_a_picture()
    if GPIO.input(27)and i==1:
        i+=1
        print("find blue color", GPIO.input(27))
        print(i)
        led_busy()
        take_a_picture()
        
    print(i)
        
def read_rgpio():
    GPIO.add_event_detect(17, GPIO.RISING, callback=event_callback, bouncetime=300)
    GPIO.add_event_detect(18, GPIO.RISING, callback=event_callback, bouncetime=300)
    GPIO.add_event_detect(22, GPIO.RISING, callback=event_callback, bouncetime=300)
    GPIO.add_event_detect(27, GPIO.RISING, callback=event_callback, bouncetime=300)


if __name__ == "__main__":
    initialise_rgpio()
    read_rgpio()
    print("end");

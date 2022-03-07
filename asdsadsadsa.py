from board import SCL, SDA
import busio
from adafruit_pca9685 import PCA9685
from adafruit_motor import servo
from time import sleep

i2c_bus = busio.I2C(SCL, SDA)
pca = PCA9685(i2c_bus)
pca.frequency = 50
maxPulse = 2500
minPulse = 600
angleInit = [5, 90, 120, 90]
angleCurrent = [0, 0, 0, 0]
angleMin = [5, 0, 50, 60]
angleMax = [65, 180, 150, 110]
angleStep = [5, 5, 8, 8]
servo0 = servo.Servo(pca.channels[0], min_pulse=600, max_pulse=2500)
servo1 = servo.Servo(pca.channels[2], min_pulse=600, max_pulse=2500)
servo2 = servo.Servo(pca.channels[3], min_pulse=600, max_pulse=2500)
servo3 = servo.Servo(pca.channels[4], min_pulse=600, max_pulse=2500)

servos =[servo0, servo1, servo2, servo3]


def initServo():
    for i in range(4):
        angleCurrent[i] = angleInit[i]
        changeAngle(i, angleInit[i])
        sleep(0.5)
    return angleCurrent
        
    
def changeAngle(servoNum, targetAngle):
    currentAngle = angleCurrent[servoNum]
    #print(currentAngle)
    
    if currentAngle <= targetAngle:
        step = angleStep[servoNum]
    elif currentAngle > targetAngle:
        step = -angleStep[servoNum]
    
    for i in range(currentAngle, targetAngle, step):
        servos[servoNum].angle = i
        #print(i)
        sleep(0.1)
        
        if i > angleMax[servoNum]:
            targetAngle = angleMax[servoNum]
            print("Max reached")
            break
        
        elif i< angleMin[servoNum]:
            targetAngle = angleMin[servoNum]
            print("Min reached")
            break
        
    servos[servoNum].angle = targetAngle
    #print(targetAngle)
    angleCurrent[servoNum] = targetAngle
    
    return angleCurrent

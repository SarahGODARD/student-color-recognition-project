from board import SCL, SDA
import busio
from adafruit_pca9685 import PCA9685
from adafruit_motor import servo
from time import sleep

class robotArm:
    def __init__(self):
        i2c_bus = busio.I2C(SCL, SDA)
        self.pca = PCA9685(i2c_bus)
        self.pca.frequency = 50
        self.maxPulse = 2500
        self.minPulse = 600
        self.angleInit = [5, 90, 50, 90]
        self.angleCurrent = [0, 0, 0, 0]
        self.angleMin = [5, 0, 50, 60]
        self.angleMax = [65, 180, 150, 110]
        self.angleStep = [5, 5, 5, 4]
        self.servo0 = servo.Servo(self.pca.channels[0], min_pulse=600, max_pulse=2500)
        self.servo1 = servo.Servo(self.pca.channels[2], min_pulse=600, max_pulse=2500)
        self.servo2 = servo.Servo(self.pca.channels[3], min_pulse=600, max_pulse=2500)
        self.servo3 = servo.Servo(self.pca.channels[4], min_pulse=600, max_pulse=2500)

        self.servos =[self.servo0, self.servo1, self.servo2, self.servo3]

    def initServo(self):
        for i in range(4):
            self.angleCurrent[i] = self.angleInit[i]
            self.changeAngle(i, self.angleInit[i])
            sleep(0.5)
        return self.angleCurrent
            
        
    def changeAngle(self, servoNum, targetAngle):
        currentAngle = self.angleCurrent[servoNum]
        #print(currentAngle)
        
        if currentAngle <= targetAngle:
            step = self.angleStep[servoNum]
        elif currentAngle > targetAngle:
            step = -self.angleStep[servoNum]
        
        for i in range(currentAngle, targetAngle, step):
            self.servos[servoNum].angle = i
            #print(i)
            sleep(0.1)
            
            if i > self.angleMax[servoNum]:
                targetAngle = self.angleMax[servoNum]
                print("Max reached")
                break
            
            elif i< self.angleMin[servoNum]:
                targetAngle = self.angleMin[servoNum]
                print("Min reached")
                break
            
        self.servos[servoNum].angle = targetAngle
        #print(targetAngle)
        self.angleCurrent[servoNum] = targetAngle
        
        return self.angleCurrent

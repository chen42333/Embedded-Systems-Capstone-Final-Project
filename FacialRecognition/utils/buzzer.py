import RPi.GPIO as GPIO
import time

class Buzzer:
    def __init__(self, pin):
        self.BuzzerPin = pin
        self.stat = False
        # GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.BuzzerPin, GPIO.OUT)
        GPIO.output(self.BuzzerPin, GPIO.LOW)

    def on(self):
        GPIO.output(self.BuzzerPin, GPIO.HIGH)    
        self.stat = True
        #低电平是响
    def off(self):
        GPIO.output(self.BuzzerPin, GPIO.LOW)
        self.stat = False
        #高电平是停止响

    def cleanup(self):
        GPIO.output(self.BuzzerPin, GPIO.LOW)
        # GPIO.cleanup()                     # Release resource
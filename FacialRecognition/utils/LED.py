import RPi.GPIO as GPIO
import time

class LEDController:
    def __init__(self, pin):
        self.pin = pin
        self.stat = False
        # GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin, GPIO.OUT)
        GPIO.output(self.pin, GPIO.LOW)
    def check(self):
        return self.stat
    def on(self):
        self.stat = True
        GPIO.output(self.pin, GPIO.HIGH)
        
    def off(self):
        self.stat = False
        GPIO.output(self.pin, GPIO.LOW)
    def cleanup(self):
        GPIO.output(self.pin, GPIO.LOW)
        # GPIO.cleanup()

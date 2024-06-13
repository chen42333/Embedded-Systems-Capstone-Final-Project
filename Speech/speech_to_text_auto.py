import RPi.GPIO as GPIO 
import time
LED_PIN = 12 
v = 343
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_PIN, GPIO.OUT)



import RPi.GPIO as GPIO
import time 
from speech_to_text import STTAgent
from linebot import LineBotApi
from linebot.models import TextSendMessage
import os
import dotenv
dotenv.load_dotenv()

v = 3434
TRIGGER_PIN = 16
ECHO_PIN = 18
GPIO.setmode(GPIO.BOARD)
GPIO.setup(TRIGGER_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN,GPIO.IN)

def measure():
    GPIO.output(TRIGGER_PIN, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(TRIGGER_PIN, GPIO.LOW)
    pulse_start = time.time()
    while GPIO.input(ECHO_PIN) == GPIO.LOW:
        pulse_start = time.time()
    while GPIO.input(ECHO_PIN) == GPIO.HIGH:
        pulse_end = time.time()
    t = pulse_end-pulse_start
    d = t*v
    d = d/2
    d = d*100
    
    return d*100
#while True:
stt = STTAgent()
    

try:
    while True:
        wait = measure()
        
        print(wait)
        if wait < 5000:
            print("start to listen")
            text = stt.run()
            if text != None:
                print(text)
                CHANNEL_ACCESS_TOKEN = os.getenv("CHANNEL_ACCESS_TOKEN")
                line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
                line_bot_api.broadcast(TextSendMessage(text = text))            
        time.sleep(1)
except KeyboardInterrupt:
    print("Exception: KeyboardInterrupt")
finally:
    GPIO.output(LED_PIN, GPIO.LOW) 
    GPIO.cleanup()

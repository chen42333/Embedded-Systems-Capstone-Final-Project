from ctypes import *
from contextlib import contextmanager
import pyaudio
import wave
import time
import speech_recognition as sr
from speech_recognition.recognizers import google, whisper

def py_error_handler(filename, line, function, err, fmt):
    pass

ERROR_HANDLER_FUNC = CFUNCTYPE(None, c_char_p, c_int, c_char_p, c_int, c_char_p)
c_error_handler = ERROR_HANDLER_FUNC(py_error_handler)

@contextmanager
def noalsaerr():
    asound = cdll.LoadLibrary('libasound.so')
    asound.snd_lib_error_set_handler(c_error_handler)
    yield
    asound.snd_lib_error_set_handler(None)

class STTAgent:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def listen(self):
        with noalsaerr():
            with sr.Microphone() as source:
                print("Please wait. Calibrating microphone...") 
                self.recognizer.adjust_for_ambient_noise(source, duration=1)
                print("Say something!")
                audio = self.recognizer.listen(source)
        return audio

    def recognize(self, audio):
        try:
            print("Google Speech Recognition thinks you said:")
            return self.recognizer.recognize_google(audio, language='zh-cn')
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            return None
        except sr.RequestError as e:
            print("No response from Google Speech Recognition service: {0}".format(e))
            return None

    def run(self):
        audio = self.listen()
        return self.recognize(audio)
        


if __name__ == '__main__':
    stt = STTAgent()
    text = stt.run()
    if text != None:
        print(text)
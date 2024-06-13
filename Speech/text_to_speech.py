from gtts import gTTS
import pygame
from io import BytesIO

def text_to_speech(text: str, lang: str ='zh') -> None:
    """
    Convert the given text to speech and play it using pygame.

    Parameters:
    text (str): The text to be converted to speech.
    lang (str): The language of the text (default is 'zh' for Chinese).

    Returns:
    None
    """
    tts = gTTS(text=text, lang=lang)
    audio_data = BytesIO()
    tts.write_to_fp(audio_data)
    audio_data.seek(0)  

    pygame.init()
    pygame.mixer.init()

    pygame.mixer.music.load(audio_data)

    pygame.mixer.music.play()

    # Wait for the audio to finish playing
    while pygame.mixer.music.get_busy():
        continue

    # Clean up Pygame resources
    pygame.mixer.quit()
    pygame.quit()

if __name__ == '__main__':
    text_to_speech("god damn")

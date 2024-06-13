from linebot import LineBotApi
from linebot.models import TextSendMessage
import dotenv
dotenv.load_dotenv()
import os

CHANNEL_ACCESS_TOKEN = os.getenv("CHANNEL_ACCESS_TOKEN")

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

def send_text(text: str):
    line_bot_api.broadcast(TextSendMessage(text = text))

if __name__ == "__main__":
    send_text("Hello, World!")

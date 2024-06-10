from linebot import LineBotApi
from linebot.models import TextSendMessage
import dotenv
dotenv.load_dotenv()
import os

CHANNEL_ACCESS_TOKEN = os.getenv("CHANNEL_ACCESS_TOKEN")

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
line_bot_api.broadcast(TextSendMessage(text = "test"))
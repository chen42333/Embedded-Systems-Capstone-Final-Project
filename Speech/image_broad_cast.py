from linebot import LineBotApi
from linebot.models import ImageSendMessage
import dotenv
dotenv.load_dotenv()
import os


# Load the channel access token from the .env file
CHANNEL_ACCESS_TOKEN = os.getenv("CHANNEL_ACCESS_TOKEN")

# Initialize the LINE Bot API with the channel access token
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

# URL of the image you want to send
image_url = 'haha.jpg'
preview_image_url = 'haha.jpg'

# Create an ImageSendMessage object
image_message = ImageSendMessage(
    original_content_url = "https://ithelp.ithome.com.tw/upload/images/20220925/20151681EaMkK6ROvq.jpg",
    preview_image_url = "https://ithelp.ithome.com.tw/upload/images/20220925/20151681EaMkK6ROvq.jpg"
)

# Broadcast the image message
line_bot_api.broadcast(image_message)

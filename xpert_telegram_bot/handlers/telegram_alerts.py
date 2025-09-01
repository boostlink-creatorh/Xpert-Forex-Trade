from config.settings import BOT_TOKEN
from telegram import Bot

bot = Bot(token=BOT_TOKEN)

def send_test_message():
    bot.send_message(chat_id='@your_test_channel_or_user_id', text='✅ Bot is connected and live!')

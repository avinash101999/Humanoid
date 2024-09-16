import logging
from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import CommandHandler, Dispatcher

# Set your token and initialize Flask
TOKEN = 'YOUR_TELEGRAM_BOT_API_TOKEN'
bot = Bot(token=TOKEN)
app = Flask(__name__)

# Initialize logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Function to handle /start command
def start(update, context):
    update.message.reply_text('Hello! I am your humanoid bot, ready to serve you!')

# Function to set up the dispatcher
def setup_dispatcher():
    dispatcher = Dispatcher(bot, None, workers=0)
    dispatcher.add_handler(CommandHandler("start", start))
    return dispatcher

dispatcher = setup_dispatcher()

# Route to receive updates from Telegram via webhook
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    update = Update.de_json(data, bot)
    dispatcher.process_update(update)
    return 'ok'

# Run the bot on the webhook
if __name__ == '__main__':
    app.run(port=8443)

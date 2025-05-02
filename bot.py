import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Define a command handler for /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello, I am your bot!')

def main():
    # Add your Telegram Bot Token here (set it as an environment variable on Koyeb)
    TOKEN = "YOUR_BOT_TOKEN_HERE"
    
    # Set up the Updater and Dispatcher
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    
    # Register command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    
    # Start polling for updates
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

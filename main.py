import logging
import os
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, CallbackContext

# Load environment variables from .env file
load_dotenv()

# Retrieve environment variables
TOKEN = os.getenv('TOKEN')
PUBLIC_URL = os.getenv('PUBLIC_URL')

# Logging setup
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Define the start command handler
async def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("Open Web App", web_app=WebAppInfo(url=PUBLIC_URL))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Hi! Click the button below to open the web app.', reply_markup=reply_markup)

# Main function to run the bot
def main() -> None:
    app = Application.builder().token(TOKEN).build()  # Create the bot application instance

    # Add command handler for the /start command
    app.add_handler(CommandHandler("start", start))

    # Start polling for updates
    app.run_polling()

if __name__ == '__main__':
    main()

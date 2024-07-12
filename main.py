import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, CallbackContext
from passwords import TOKEN, PUBLIC_URL

# Логирование
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Функция для команды /start
async def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("Open Web App", web_app=WebAppInfo(url=PUBLIC_URL))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Привет! Нажмите кнопку ниже, чтобы открыть веб-приложение.', reply_markup=reply_markup)

# Основная функция для запуска бота
def main() -> None:
    # Создаем экземпляр приложения
    app = Application.builder().token(TOKEN).build()

    # Добавляем обработчик команды /start
    app.add_handler(CommandHandler("web", start))

    # Запускаем бота
    app.run_polling()

if __name__ == '__main__':
    main()

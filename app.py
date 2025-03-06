import os
import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# ✅ Cấu hình logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# ✅ Lấy TOKEN từ biến môi trường
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# ✅ Hàm xử lý lệnh /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Hello! Bot is running on Render 🚀")

# ✅ Hàm xử lý tin nhắn
def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)

def main():
    # ✅ Khởi tạo bot với polling (Render không hỗ trợ Webhook miễn phí)
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()

from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram.ext import ConversationHandler, CallbackQueryHandler
from telegram import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

# Khai báo các trạng thái (state) trong conversation
NAME, PHONE_NUMBER = range(2)

# Xử lý lệnh /start
def start(update: Update, context: CallbackContext):
    update.message.reply_text('Xin chào! Vui lòng chia sẻ thông tin của bạn.')
    return NAME

def huy(update: Update, context: CallbackContext):
    update.message.reply_text('Xin chào! Vui lòng chia sẻ thông tin của bạn.')
    return NAME

# Xử lý khi người dùng nhấn nút "Chia sẻ thông tin"
def share_info(update: Update, context: CallbackContext):
    keyboard = [
        [KeyboardButton("Chia sẻ thông tin", request_contact=True)]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
    update.message.reply_text('Vui lòng chia sẻ thông tin của bạn.', reply_markup=reply_markup)
    return PHONE_NUMBER

# Xử lý khi người dùng chia sẻ thông tin (số điện thoại)
def handle_info(update: Update, context: CallbackContext):
    phone_number = update.message.contact.phone_number
    update.message.reply_text(f"Số điện thoại của bạn là: {phone_number}")

    # Lưu thông tin vào database hoặc xử lý theo nhu cầu của bạn

    # return ConversationHandler.END

# Thiết lập và chạy bot
def main():
    updater = Updater('6343669796:AAFcB4Vq4PmCzr4W1ZJQwAYyjMWLwwwIW-k', use_context=True)
    dispatcher = updater.dispatcher

    # Thiết lập ConversationHandler để xử lý conversation
    conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start)],
    states={
        NAME: [MessageHandler(Filters.text, share_info)],
        PHONE_NUMBER: [MessageHandler(Filters.contact, handle_info)],
    },
    fallbacks=[CommandHandler('huy', huy)],
    )
    
    dispatcher.add_handler(conv_handler)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
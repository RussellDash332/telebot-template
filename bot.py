from env import TOKEN
from telegram.ext import Updater, CommandHandler # MessageHandler, filters

def start(update, context):
    # See README.md for more context
    print(update)
    update.message.reply_text('Lorem ipsum')

if __name__ == '__main__':
    # To get bot updates, go to https://api.telegram.org/bot{TOKEN}/getUpdates
    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher

    # List of commands that we can do!
    dp.add_handler(CommandHandler("start", start))    # run the start function if the message is /start

    updater.start_polling()
    print("++++++++++ STARTING BOT +++++++++++")
    updater.idle()
    print("++++++++++  KILLING BOT  ++++++++++")
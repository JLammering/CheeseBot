from telegram.ext import Updater
import logging
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters






def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Willkommen im MarktBestellBot.")

def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Entschuldigung, den Befehl hab ich nicht verstanden.")





def main():
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

    token_file = open("token.txt", "r")
    token = token_file.read().splitlines()[0]


    updater = Updater(token=token, use_context=True)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    unknown_handler = MessageHandler(Filters.command, unknown)
    dispatcher.add_handler(unknown_handler)

    updater.start_polling()

if __name__ == '__main__':
    main()

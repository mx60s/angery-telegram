import logging
from telegram.ext import Updater, MessageHandler, Filters, BaseFilter


token_file = open("api_token.txt", "r")

TOKEN = token_file.readline().strip()


class QuietFilter(BaseFilter):
    def filter(self, message):
        return 'no' == message.text.strip() or 'No' == message.text.strip()

class LoudFilter(BaseFilter):
    def filter(self, message):
        return 'NO' == message.text.strip()

class YesFilter(BaseFilter):
    def filter(self, message):
        return 'yes' == message.text.strip().lower()

def get_angery(update, context):
    context.bot.send_photo(chat_id=update.message.chat_id,
                              photo=open('kitty.jpeg', 'rb'))

def get_furious(update, context):
    context.bot.send_photo(chat_id=update.message.chat_id,
                              photo=open('kitty_closeup.jpeg', 'rb'))

def get_nasty(update, context):
    context.bot.send_photo(chat_id=update.message.chat_id, photo=open('yes.jpeg', 'rb'))

def unknown(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,
                              text='who knows man')


def main():
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)

    quiet = QuietFilter()
    loud = LoudFilter()
    yes = YesFilter()

    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    anger_handler = MessageHandler(Filters.text & quiet, get_angery)
    fury_handler = MessageHandler(Filters.text & loud, get_furious)
    yes_handler = MessageHandler(Filters.text & yes, get_nasty)
    dispatcher.add_handler(anger_handler)
    dispatcher.add_handler(fury_handler)
    dispatcher.add_handler(yes_handler)

    updater.start_polling()


if __name__ == "__main__":
    main()

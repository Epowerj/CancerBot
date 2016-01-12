from telegram import Updater
from key import apikey


def start(bot, update):
    bot.sendMessage(update.message.chat_id, text='Hi!')


def help(bot, update):
    bot.sendMessage(update.message.chat_id, text='Just ask @Epowerj')


def ping(bot, update):
    bot.sendMessage(update.message.chat_id, text='Pong')


def error(bot, update, error):
    print('Update "%s" caused error "%s"' % (update, error))


def main():
    updater = Updater(apikey)
    dp = updater.dispatcher

    dp.addTelegramCommandHandler("start", start)
    dp.addTelegramCommandHandler("help", help)
    dp.addTelegramCommandHandler("ping", ping)

    # dp.addTelegramMessageHandler(tally)

    dp.addErrorHandler(error)
    updater.start_polling(timeout=5)

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT
    updater.idle()

if __name__ == '__main__':
    main()
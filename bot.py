from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
from key import apikey
import datetime


def start(bot, update):
    bot.sendMessage(update.message.chat_id, text="Oh hello, I didn't see you there")


def help(bot, update):
    bot.sendMessage(update.message.chat_id, text='Just ask @Epowerj')


def test(bot, update):
    bot.sendMessage(update.message.chat_id, text='Even now, the evil seed of what you have done')
    bot.sendMessage(update.message.chat_id, text='G E R M I N A T E S')
    bot.sendMessage(update.message.chat_id, text='within you...')


def ping(bot, update):
    bot.sendMessage(update.message.chat_id, text='Pong')


def boat(bot, update):
    bot.sendMessage(update.message.chat_id, text="You don't deserve a boat, take this log instead")


def time(bot, update):
    bot.sendMessage(update.message.chat_id, text=str(datetime.datetime.now()))
    tally(bot, update)


def error(bot, update, error):
    print('Update "%s" caused error "%s"' % (update, error))


def main():
    updater = Updater(apikey)
    dp = updater.dispatcher

    dp.addTelegramCommandHandler("start", start)
    dp.addTelegramCommandHandler("help", help)
    dp.addTelegramCommandHandler("test", test)
    dp.addTelegramCommandHandler("ping", ping)
    dp.addTelegramCommandHandler("time", time)
    dp.addTelegramCommandHandler("boat", boat)

    dp.addErrorHandler(error)

    updater.start_polling(timeout=5)

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    main()

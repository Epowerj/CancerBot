from telegram import Updater
from key import apikey

import datetime
import fortune


def start(bot, update):
    bot.sendMessage(update.message.chat_id, text='Hi!')


def help(bot, update):
    bot.sendMessage(update.message.chat_id, text='Just ask @Epowerj')


def test(bot, update):
    bot.sendMessage(update.message.chat_id, text='The evil seed of what you have done')
    bot.sendMessage(update.message.chat_id, text='G E R M I N A T E S')
    bot.sendMessage(update.message.chat_id, text='within you...')


def ping(bot, update):
    bot.sendMessage(update.message.chat_id, text='Pong')


def boat(bot, update):
    bot.sendMessage(update.message.chat_id, text="You don't deserve a boat, take this log instead")


def time(bot, update):
    bot.sendMessage(update.message.chat_id, text=str(datetime.datetime.now()))


def cookie(bot, update):
    # bot.sendMessage(update.message.chat_id, text='Getting your fortune...')
    out = fortune.get_random_fortune('/home/pi/CancerBot/fortunes/fortunes')
    bot.sendMessage(update.message.chat_id, text=out)


def error(bot, update, error):
    print('Update "%s" caused error "%s"' % (update, error))


def events(bot, update):
    bot.sendMessage(update.message.chat_id, text="Upcoming Events: \n" +
                                                 "Cancer Anniversary - https://gist.github.com/Epowerj/ea2c883bcb14516fd99d")


def gaming(bot, update):
    bot.sendMessage(update.message.chat_id, text="CCentral Gaming Info: \n" +
                                                 "https://gist.github.com/Epowerj/4f200ee4af54042a0b11")


def main():
    updater = Updater(apikey)
    dp = updater.dispatcher

    dp.addTelegramCommandHandler("start", start)
    dp.addTelegramCommandHandler("help", help)
    dp.addTelegramCommandHandler("test", test)
    dp.addTelegramCommandHandler("ping", ping)
    dp.addTelegramCommandHandler("time", time)
    dp.addTelegramCommandHandler("boat", boat)
    dp.addTelegramCommandHandler("cookie", cookie)
    dp.addTelegramCommandHandler("events", events)
    dp.addTelegramCommandHandler("gameing", gaming)

    # dp.addTelegramMessageHandler(tally)

    dp.addErrorHandler(error)
    updater.start_polling(timeout=5)

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT
    updater.idle()

if __name__ == '__main__':
    main()
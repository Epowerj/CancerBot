from telegram import Updater
from key import apikey
import datetime

fortuneDb = "/home/epowerj/Public/fortunes/fortunes"

def tally(bot, update):
    botan_token = '9b30424f-889e-4608-a17c-fa1accc40913' # Token got from @botaniobot
    uid = update.message.from_user
    message_dict = update.message.to_dict()
    event_name = update.message.text
    #print(botan.track(botan_token, uid, message_dict, event_name))


def kek_kounter(bot, update):
    if update.message.text == 'kek' or update.message.text == 'kek!':
        tally(bot, update)


def start(bot, update):
    bot.sendMessage(update.message.chat_id, text='Hi!')
    tally(bot, update)


def help(bot, update):
    bot.sendMessage(update.message.chat_id, text='Just ask @Epowerj')
    tally(bot, update)


def test(bot, update):
    bot.sendMessage(update.message.chat_id, text='Even now, the evil seed of what you have done')
    bot.sendMessage(update.message.chat_id, text='G E R M I N A T E S')
    bot.sendMessage(update.message.chat_id, text='within you...')
    tally(bot,update)


def ping(bot, update):
    bot.sendMessage(update.message.chat_id, text='Pong')
    tally(bot, update)


def boat(bot, update):
    bot.sendMessage(update.message.chat_id, text="You don't deserve a boat, take this log instead")
    tally(bot, update)


def time(bot, update):
    bot.sendMessage(update.message.chat_id, text=str(datetime.datetime.now()))
    tally(bot, update)


def error(bot, update, error):
    print('Update "%s" caused error "%s"' % (update, error))


def events(bot, update):
    bot.sendMessage(update.message.chat_id, disable_web_page_preview=True, text="Upcoming Events: \n" +
                                                 "Cancer Anniversary - https://gist.github.com/Epowerj/ea2c883bcb14516fd99d")
    tally(bot, update)


def gaming(bot, update):
    bot.sendMessage(update.message.chat_id, disable_web_page_preview=True, text="CCentral Gaming Info: \n" +
                                                 "https://gist.github.com/Epowerj/4f200ee4af54042a0b11")
    tally(bot, update)


def main():
    updater = Updater(apikey)
    dp = updater.dispatcher

    dp.addTelegramCommandHandler("start", start)
    dp.addTelegramCommandHandler("help", help)
    dp.addTelegramCommandHandler("test", test)
    dp.addTelegramCommandHandler("ping", ping)
    dp.addTelegramCommandHandler("time", time)
    dp.addTelegramCommandHandler("boat", boat)
    dp.addTelegramCommandHandler("events", events)
    dp.addTelegramCommandHandler("gaming", gaming)
    dp.addTelegramMessageHandler(kek_kounter)

    dp.addErrorHandler(error)

    updater.start_polling(timeout=5)

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    main()

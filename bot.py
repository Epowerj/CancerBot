from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
from key import apikey
import datetime, json

meme_waiting = False
memers = {}

savepath = "memers.dict"

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)


def load_memers():
    global memers

    save = open(savepath, 'r')
    memers = json.load(save)


def save_memers():
    save = open(savepath, 'w')
    json.dump(memers, save)


def start(bot, update):
    bot.sendMessage(update.message.chat_id, text="Why hello, I didn't see you there")


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


def chatinfo(bot, update):
    bot.sendMessage(update.message.chat_id, text="chat_id is "+str(update.message.chat_id))
    bot.sendMessage(update.message.chat_id, text="user id is "+str(update.message.from_user.id))


def incrementMemer(user):
    if (user in memers):
        memers[user] += 1
    else:
        memers[user] = 0
        memers[user] += 1

    save_memers()
    

def ebin(bot, update):
    if meme_waiting:
        bot.sendMessage(update.message.chat_id, text=update.message.from_user.first_name+" caught the meme!")
        incrementMemer(str(update.message.from_user.id))
        #set meme_waiting to false

def stats(bot, update):
    if (str(update.message.from_user.id) in memers):
        bot.sendMessage(update.message.chat_id, text=update.message.from_user.first_name+" has "+str(memers[str(update.message.from_user.id)]))
    else:
        bot.sendMessage(update.message.chat_id, text=update.message.from_user.first_name+" has 0")


def error(bot, update, error):
    print('Update "%s" caused error "%s"' % (update, error))


def main():
    print("memers default value:")
    print(memers)

    load_memers()

    print("loaded memers:")
    print(memers)

    updater = Updater(apikey)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("test", test))
    dp.add_handler(CommandHandler("ping", ping))
    dp.add_handler(CommandHandler("time", time))
    dp.add_handler(CommandHandler("boat", boat))
    dp.add_handler(CommandHandler("ebin", ebin))
    dp.add_handler(CommandHandler("stats", stats))
    dp.add_handler(CommandHandler("chatinfo", chatinfo))

    dp.add_error_handler(error)

    updater.start_polling(timeout=5)

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    main()

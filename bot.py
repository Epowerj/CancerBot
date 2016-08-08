
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
from key import apikey
import datetime, json, random, time

meme_waiting = 0
memers = {}
# gifts = {} TODO count gifts

savepath = "memers.dict"

ccentral_id = -1001044604031

hoptidote_cooldown = time.monotonic()

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
    bot.sendMessage(update.message.chat_id, text="""Even now, the evil seed of what you have done
G E R M I N A T E S
within you...""")


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
    global meme_waiting
    global ccentral_id

    if meme_waiting > 0 and update.message.chat_id == ccentral_id:
        bot.sendMessage(update.message.chat_id, text=update.message.from_user.first_name+" caught the meme!")
        incrementMemer(str(update.message.from_user.id))
        meme_waiting -= 1
    else:
        bot.sendMessage(update.message.chat_id, text="There is no meme to catch")


def stats(bot, update):
    if (str(update.message.from_user.id) in memers):
        bot.sendMessage(update.message.chat_id, text=update.message.from_user.first_name+" has " + str(memers[str(update.message.from_user.id)]) + " ebins")
    else:
        bot.sendMessage(update.message.chat_id, text=update.message.from_user.first_name+" has 0 ebins")


def memegrab(bot):
    global meme_waiting

    meme_waiting += 1
    bot.sendMessage(ccentral_id, text="A wild meme has appeared! Do /ebin to catch it!")
    sleep(random.randint(0, 5400))


def hoptidote(bot, update): #TODO add timeout
    import time
    global hoptidote_cooldown

    symptoms = {'normie', 'suffering', 'misery', 'comfy'}
    antidotes = {27511, 27512, 27513, 27514, 27515, 27516, 27517, 27518, 27519, 27520, 27521, 27522, 27523, 27524, 27525, 
                 27526, 27527, 27528, 27529, 27530, 27531, 27532, 27533, 27534, 27535, 27536, 27537, 27538, 27539, 27540,
                 27541, 27542, 27543, 27544, 27545, 27546, 27547, 27548}

    if update.message.from_user.id == 94250469 and (time.monotonic()-hoptidote_cooldown) > 600:
        hoptidote_cooldown = time.monotonic()
        for symptom in symptoms:
            if symptom in update.message.text:
                bot.forward_message(chat_id=update.message.chat_id, message_id=antidotes[random.randint(0, antidotes.length)])
                break


def drop(bot, update):
    global meme_waiting
    
    if memers[str(update.message.from_user.id)] > 0:
        memers[str(update.message.from_user.id)] -= 1
        meme_waiting += 1
        bot.sendMessage(ccentral_id, text=update.message.from_user.first_name+" has dropped a meme! Use /ebin to catch it!")
    else:
        bot.sendMessage(update.message.chat_id, text="You're out of ebins")


def gift(bot, update): #TODO
    if memers[str(update.message.from_user.id)] > 0:
        commandtext = update.message.text.split(' ', 1)[1]
        
        memers[str(update.message.from_user.id)] -= 1


def top(bot, update):
    global memers
    import operator
    sorted_memers = sorted(memers.items(), key=operator.itemgetter(1))
    
    toplist = ""
    for memer in sorted_memers:
        toplist += memer+"\n"

    bot.sendMessage(updage.message.chat_id, text=toplist)


def parse(bot, update):
    #print(update.message.message_id)
    hoptidote(bot, update)


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
    jqueue = updater.job_queue

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("test", test))
    dp.add_handler(CommandHandler("ping", ping))
    dp.add_handler(CommandHandler("time", time))
    dp.add_handler(CommandHandler("boat", boat))
    dp.add_handler(CommandHandler("ebin", ebin))
    dp.add_handler(CommandHandler("stats", stats))
    dp.add_handler(CommandHandler("chatinfo", chatinfo))
    dp.add_handler(CommandHandler("drop", drop))

    dp.add_handler(MessageHandler([Filters.text], parse))

    dp.add_error_handler(error)

    updater.start_polling(timeout=5)
    
    # Wild meme generation
    #jqueue.put(memegrab, 1800, next_t=0)

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    main()

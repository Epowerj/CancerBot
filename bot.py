
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import logging
from key import apikey
import datetime, json, random, time

meme_waiting = 0
memers = {}
lottery_jackpot = 30

savepath = "memers.dict"

ccentral_id = -1001044604031

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

def give_ebins(user, amount):
    if (user in memers):
        memers[user] += amount
        save_memers()
    else:
        memers[user] = amount
        save_memers()
        
    
def charge_ebins(user, amount):    
    if (user in memers):
        if memers[user] >= amount:
            memers[user] -= amount
            save_memers()
            return True
        else:
            return False
    else:
        memers[user] = 0
        save_memers()
        return False
        

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


def hoptidote(bot, message): #TODO add timeout
    import time

    antidotes = [27511, 27512, 27513, 27514, 27515, 27516, 27517, 27518, 27519, 27520, 27521, 27522, 27523, 27524, 27525, 
                 27526, 27527, 27528, 27529, 27530, 27531, 27532, 27533, 27534, 27535, 27536, 27537, 27538, 27539, 27540,
                 27541, 27542, 27543, 27544, 27545, 27546, 27547, 27548, 27654]

    bot.forward_message(chat_id=message.chat_id, from_chat_id=83218061, message_id=antidotes[random.randint(0,  len(antidotes))])


def drop(bot, update):
    global meme_waiting
    
    if memers[str(update.message.from_user.id)] > 0:
        memers[str(update.message.from_user.id)] -= 1
        meme_waiting += 1
        bot.sendMessage(ccentral_id, text=update.message.from_user.first_name+" has dropped a meme! Use /ebin to catch it!")
    else:
        bot.sendMessage(update.message.chat_id, text="You're out of ebins")


def shop(bot, update):
    global lottery_jackpot
    
    keyboard = [[InlineKeyboardButton("Tux Cringe [5e]", callback_data='1'),
                 InlineKeyboardButton("Interesting SFX [5e]", callback_data='2')],
                [InlineKeyboardButton("Lottery [2e] - Current Jackpot: "+ str(lottery_jackpot), callback_data='3')]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    bot.sendMessage(update.message.chat_id, text="Loabot's Wares:", reply_markup=reply_markup)

    
def shopbutton(bot, update):
        query = update.callback_query

        selection = query.data

        #bot.editMessageText(text="Thank you for your purchase, "+query.from_user.first_name,
        #                    chat_id=query.message.chat_id, message_id=query.message.message_id)

        if selection == '1':
            if charge_ebins(str(query.from_user.id), 5):
                bot.editMessageText(text="Thank you for your purchase, "+query.from_user.first_name,
                            chat_id=query.message.chat_id, message_id=query.message.message_id)
                
                hoptidote(bot, query.message)
            else:
                bot.editMessageText(text="Sorry "+query.from_user.first_name+", you don't have enough ebins",
                            chat_id=query.message.chat_id, message_id=query.message.message_id)
        elif selection == '2':
            if charge_ebins(str(query.from_user.id), 5):
                bot.editMessageText(text="Thank you for your purchase, "+query.from_user.first_name,
                            chat_id=query.message.chat_id, message_id=query.message.message_id)
                
                print('in progress')
            else:
                bot.editMessageText(text="Sorry "+query.from_user.first_name+", you don't have enough ebins",
                            chat_id=query.message.chat_id, message_id=query.message.message_id)
        elif selection == '3':
            if charge_ebins(str(query.from_user.id), 2):
                bot.editMessageText(text="Thank you for your purchase, "+query.from_user.first_name,
                            chat_id=query.message.chat_id, message_id=query.message.message_id)
            
                lottery(bot, query.message, query.from_user)
            else:
                bot.editMessageText(text="Sorry "+query.from_user.first_name+", you don't have enough ebins",
                            chat_id=query.message.chat_id, message_id=query.message.message_id)
    
            
def lottery(bot, message, user):
    global lottery_jackpot

    roll = random.randint(1, 100)

    lottery_jackpot += 2
    
    if roll == 100:
        give_ebins(user.id, lottery_jackpot)
        bot.sendMessage(message.chat_id, text=user.first_name+" hit the jackpot!! "+str(lottery_jackpot)+" ebins awarded!")
        lottery_jackput = 30
    else:
        bot.sendMessage(message.chat_id, text="Sorry "+user.first_name+", you got a "+str(roll)+" - Get a 100 to win the jackpot")
        
        
def parse(bot, update):
    print("Message from " + update.message.from_user.first_name + "(" + str(update.message.from_user.id) + "): " + update.message.text + " (" + str(update.message.message_id) + ")")
    if "boat" in update.message.text:
        bot.sendMessage(update.message.chat_id, text="You don't deserve a boat, have this log instead")


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
    dp.add_handler(CommandHandler("shop", shop))
    updater.dispatcher.add_handler(CallbackQueryHandler(shopbutton))

    dp.add_handler(MessageHandler([Filters.text], parse))

    dp.add_error_handler(error)

    updater.start_polling(timeout=5)
    
    # Wild meme generation
    #jqueue.put(memegrab, 1800, next_t=0)

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging
import copy

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

Minus_ID_number = int(245461326)
Avet_ID_number = int(345461326)

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Ah, hola, quien eres?')
    print("------- Start Message --------")
    print(update.message.chat)
    print(update.message.text)
    print("---------------------")
    Chat_Number = int(update.message.chat.id)
    Chat_Name = str(update.message.chat.first_name) +" "+ str(update.message.chat.last_name)
    Echo = update
    Echo.message.chat.id = Minus_ID_number
    Echo_Answer = "Unidentified message from: \n" + Chat_Name+ "\n"+ str(Chat_Number) + "\n \n" + 'Is trying to start talking'
    Echo.message.reply_text(Echo_Answer)




def Minus_ID(update):
    """Echo the user message."""
    print("------- New Message --------")
    print(update.message.chat)
    print(update.message.text)
    #print(*update.message.photo, sep = "\n")
    print("---------------------")
    Echo = update
    Echo.message.chat.id = Avet_ID_number

    if len(update.message.photo) < 1:
        Echo.message.reply_text(update.message.text)

    else:
        print("Picture")
        Echo.message.reply_photo(update.message.photo[-1].file_id)

def Avet_ID(update):
    """Echo the user message."""
    print("------- New Message --------")
    print(update.message.chat)
    print(update.message.text)
    print("---------------------")
    Echo = update
    Echo.message.chat.id = Minus_ID_number
    if len(update.message.photo) < 1:
        Echo.message.reply_text(update.message.text)

    else:
        print("Picture")
        Echo.message.reply_photo(update.message.photo[-1].file_id)


def Wrong_ID(update):
    """Echo the user message."""
    print("------- Unidentified Message --------")
    print(update.message.chat)
    print(update.message.text)
    print("---------------------")
    Chat_Number = int(update.message.chat.id)
    Chat_Name = str(update.message.chat.first_name) +" "+ str(update.message.chat.last_name)
    Echo = update
    Echo.message.chat.id = Minus_ID_number
    Echo_Answer = "Unidentified message from: \n" + Chat_Name+ "\n"+ str(Chat_Number) + "\n \n" + str(update.message.text)
    if len(update.message.photo) < 1:
        Echo.message.reply_text(Echo_Answer)

    else:
        Echo.message.reply_text(Echo_Answer)
        Echo.message.reply_photo(update.message.photo[-1].file_id)

def ID_Selection(update,context):
    if int(update.message.chat.id) == Avet_ID_number:
        print('Avet Talking')
        print(Avet_ID_number)
        print(update.message.chat)
        return(Avet_ID(update))

    elif int(update.message.chat.id) == Minus_ID_number:
        print('Martí Talking')
        print(Minus_ID_number)
        print(update.message.chat)
        return(Minus_ID(update))

    else:
        print('Somebody Talking')
        print(Avet_ID_number)
        print(update.message.chat)
        return(Wrong_ID(update))

def Set_ID(update, context):
    New_ID = update.message.text
    New_ID = New_ID.replace("/Set_ID ","")
    if len(New_ID) > 7:
        Answer = ("New Avet ID: " + str(New_ID))
        print(Answer)
        global Avet_ID_number
        Avet_ID_number = int(New_ID)
        update.message.reply_text(Answer)
    else:
        Answer = ("Wrong ID Format")
        print(Answer)
        update.message.reply_text(Answer)

def Get_ID(update, context):
    global Avet_ID_number
    Answer = ("Current Avet ID: " + str(Avet_ID_number))
    print(Answer)
    update.message.reply_text(Answer)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def Echo_Cannot_Understand(update, context):
    update.message.reply_text('Lo siento pero de momento solo entiendo texto e imagenes, si me envias audios o stickers no puedo entenderte :(')
    print('Tried to send something other than text or picture')

def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("1793883774:AAH4GfONOWXHeLj5RDMRGtkrXRppDw6xWE8", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("Set_ID", Set_ID))
    dp.add_handler(CommandHandler("Get_ID", Get_ID))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text | Filters.photo, ID_Selection))
    dp.add_handler(MessageHandler(~Filters.text & ~ Filters.photo & ~ Filters.command, Echo_Cannot_Understand))


    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()

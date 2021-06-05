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

Minus_ID_number = 245461326
Avet_ID_number = 706549700

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Ah, hola, quien eres?')


def Minus_ID(update):
    """Echo the user message."""
    print("------- New Message --------")
    print(update.message.chat)
    print(update.message.text)
    print("---------------------")
    Echo = update
    Echo.message.chat.id = Avet_ID_number
    Echo.message.reply_text(update.message.text)

def Avet_ID(update):
    """Echo the user message."""
    print("------- New Message --------")
    print(update.message.chat)
    print(update.message.text)
    print("---------------------")
    Echo = update
    Echo.message.chat.id = Minus_ID_number
    Echo.message.reply_text(update.message.text)

def Wrong_ID(update):
    """Echo the user message."""
    print("------- Unidentified Message --------")
    print(update.message.chat)
    print(update.message.text)
    print("---------------------")
    Chat_Number = int(update.message.chat.id)
    Echo = update
    Echo.message.chat.id = Minus_ID_number
    Echo_Answer = "Unidentified message from: \n" +str(Chat_Number) + "\n \n" + str(update.message.text)
    Echo.message.reply_text(Echo_Answer)

def ID_Selection(update,context):
    if update.message.chat.id == Avet_ID_number: return(Avet_ID(update))
    elif update.message.chat.id == Minus_ID_number: return(Minus_ID(update))
    else: return(Wrong_ID(update))

def Set_ID(update, context):
    New_ID = update.message.text
    New_ID = New_ID.replace("/Set_ID ","")
    if len(New_ID) == 9:
        Answer = ("New Avet ID: " + str(New_ID))
        print(Answer)
        global Avet_ID_number
        Avet_ID_number = New_ID
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
    dp.add_handler(MessageHandler(Filters.text, ID_Selection))


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

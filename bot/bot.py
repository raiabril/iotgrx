#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
iotGRX bot

This is the bot to retrive the chat id of the users we want to notify.

Requires:
    :env TOKEN - Telegram Token to be passed as env variable.


"""

import logging
import os
import sqlite3
from datetime import datetime
from dotenv import load_dotenv

from telegram import Update
from telegram.ext import (CallbackContext,
                          CommandHandler, Filters, MessageHandler, Updater)

# Enable the logger
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


# Load the environment variables
load_dotenv()


def insert_message(created_at, update_id, chat_id, username, text, first_name, last_name, link):
    """" Function to insert the message into the database."""

    con = sqlite3.connect('example.db')
    cursor = con.cursor()
    sql = "INSERT INTO messages (created_at, update_id, chat_id, username, text, first_name, last_name, link) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
    val = (created_at.__str__(), update_id, chat_id,
           username, text, first_name, last_name, link)
    cursor.execute(sql, val)
    con.commit()
    cursor.close()
    con.close()


def start(update: Update, context: CallbackContext):
    """ Function to update the user when the /start command is received. """

    context.bot.send_message(
        chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


def message_handler(bot, update):
    """ Function to handle all the messages from the user. """

    insert_message(
        update_id=bot.update_id, 
        created_at=datetime.now(), 
        text=bot.effective_message.text,
        chat_id=bot.effective_user.id, 
        username=bot.effective_user.username,
        first_name=bot.effective_user.first_name, 
        last_name=bot.effective_user.last_name, 
        link=bot.effective_user.link)


def error(bot, update, error):
    """ Function to manage errors. """

    # Log Errors caused by Updates.
    logger.warning('Error: "%s" caused error "%s"', update, error)
    logger.setLevel(logging.DEBUG)


def main():
    """ Main function of the bot."""

    # Initialize database if not exsiting.
    con = sqlite3.connect('example.db')
    cursor = con.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS messages
                         (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                          created_at TEXT, 
                          update_id INTEGER NOT NULL,
                          chat_id INTEGER NOT NULL, 
                          username TEXT,
                          first_name TEXT, 
                          last_name TEXT, 
                          link TEXT,
                          text TEXT)''')

    con.commit()
    cursor.close()
    con.close()

    # Create the Updater
    updater = Updater(os.environ.get('TOKEN'))

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add handlers
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.text, message_handler))

    # Handler to log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()


if __name__ == '__main__':
    main()

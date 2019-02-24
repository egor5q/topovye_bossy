# -*- coding: utf-8 -*-
import os
import telebot
import time
import random
import threading
from emoji import emojize
from telebot import types
from pymongo import MongoClient
import unit_classes


token = os.environ['TELEGRAM_TOKEN']
bot = telebot.TeleBot(token)


client=MongoClient(os.environ['database'])
db=client.
users=db.users

        
        

def createuser(user):
    return {
        'id':user.id,
        'name':user.first_name,
        'username':user.username
    }
        
        
print('7777')
bot.polling(none_stop=True,timeout=600)


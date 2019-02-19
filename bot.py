# -*- coding: utf-8 -*-
import os
import telebot
import time
import random
import threading
from emoji import emojize
from telebot import types
from pymongo import MongoClient


token = os.environ['TELEGRAM_TOKEN']
bot = telebot.TeleBot(token)


client=MongoClient(os.environ['database'])
db=client.
users=db.users

@bot.message_handler(commands=['createboss'])
def createboss(m):
    x=users.find({})
    reg=False
    for ids in x:
        if ids['id']==m.from_user.id:
            reg=True
    if reg==False:
        users.insert_one(createuser(m.from_user))
    user=users.find_one({'id':m.from_user.id})
    if user['createcount']>0:
        try:
            x=m.text.split(' ')[1]
        except:
            x=None
        if x!=None:
            if x.lower()=='танк':
                unit=unit_classes.Tank()
            elif x.lower()=='хилер':
                unit=unit_classes.Healer()
            elif x.lower()=='дамагер':
                unit=unit_classes.Damager()
            elif x.lower()=='универсал':
                unit=unit_classes.Universal()
            bot.send_message(m.chat.id, 'Теперь отправьте характеристики вашего босса.')
        
        

def createuser(user):
    return {
        'id':user.id,
        'name':user.first_name,
        'username':user.username,
        'createdbosses':{},
        'createcount':8
    }
        
        
print('7777')
bot.polling(none_stop=True,timeout=600)


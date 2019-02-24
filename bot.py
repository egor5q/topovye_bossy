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
db=client.futurewars
users=db.users

tanks=[unit_classes.Test]
turrets=[unit_classes.Test1]
robots=[unit_classes.Test2]
weapons=[unit_classes.Test3]


@bot.message_handler(commands=['start'])
def start(m):
    tutorial=0
    if m.from_user.id==m.chat.id:
        if users.find_one({'id':m.from_user.id})==None:
            users.insert_one(createuser(m.from_user))
            tutorial=1
        user=users.find_one({'id':m.from_user.id})
        if tutorial==1:
            bot.send_message(m.chat.id, 'Игра "FutureWars". Здесь ты будешь прокачивать свою армию, собирая роботов, турели и танки, и '+
                             'нанимая солдат! Добывай руды, отбивайся от атак соперника и укрепляй свою военную базу!')
            
    
@bot.message_handler(commands=['build'])
def army(m):
    buildmenu(m.from_user)
        

def buildmenu(user, m=None):
    text='Выберите категорию для сборки:'
    kb=types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton(text='Роботы', callback_data='buildrobots'), types.InlineKeyboardButton(text='Танки', callback_data='buildtanks'))
    kb.add(types.InlineKeyboardButton(text='Турели', callback_data='buildturrets'), types.InlineKeyboardButton(text='Оружие', callback_data='buildweapons'))
    if m==None:
        bot.send_message(user.id, text, reply_markup=kb)
    else:
        medit(text, m.chat.id, m.message_id, reply_markup=kb)
         
       
    
@bot.callback_query_handler(func=lambda call:True)
def inline(call):
    kb=types.InlineKeyboardMarkup()
    if 'build' in call.data:
        if 'robots' in call.data:
            spisok=robots
            name='робота'
        elif 'tanks' in call.data:
            spisok=tanks
            'танк'
        elif 'turrets' in call.data:
            spisok=turrets
            name='турель'
        elif 'weapons' in call.data:
            spisok=weapons
            name='оружие'
        for ids in spisok:
            item=ids()
            kb.add(types.InlineKeyboardButton(text=item.name, callback_data='show '+item.data))
        medit('Выберите '+name+' для просмотра:', call.message.chat.id, call.message.message_id, reply_markup=kb)
            
    
        
def createuser(user):
    return {
        'id':user.id,
        'name':user.first_name,
        'username':user.username,
        'army':[],
        'weapons':[],
        'money':100,
        'iron':100,
        'buildings':[]
    }
        
        
print('7777')
bot.polling(none_stop=True,timeout=600)


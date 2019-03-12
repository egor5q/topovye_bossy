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
import game_classes
from tools import medit


token = os.environ['TELEGRAM_TOKEN']
bot = telebot.TeleBot(token)


client=MongoClient(os.environ['database'])
db=client.futurewars
users=db.users

tanks=[unit_classes.Breaker]
turrets=[unit_classes.Multigun]
robots=[unit_classes.Lazerbot]

weapons=[unit_classes.Test3]
classes=[]

for ids in tanks:
    classes.append(ids)
for ids in turrets:
    classes.append(ids)
for ids in robots:
    classes.append(ids)
for ids in weapons:
    classes.append(ids)


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
            
            
@bot.message_handler(content_types=['photo'])
def photo(m):
    if m.from_user.id==m.chat.id:
        bot.send_photo(441399484, m.photo[0].file_id, caption=str(m.photo[0].file_id))
            
            
@bot.message_handler(commands=['testfight'])
def testfight(m):
    player1=441399484
    player2=22
    players=[player1, player2]
    addteams(players)
        
def addteams(players):
    team1={'army':{}}
    team2={'army':{}}
    for ids in classes:
        item=ids()
        if item.type!='weapon':
            team1.army.update({item.id:item})
    team1.update({'player':createplayer(441399484)})
    for ids in classes:
        item=ids()
        if item.type!='weapon':
            team2.army.update({item.id:item})
    team2.update(createplayer(None))
    teams=[team1, team2]
    game=game_classes.Game()
    users=[]
    game.createteams(teams)
    game.startgame()
        
        
@bot.message_handler(commands=['build'])
def army(m):
    buildmenu(m.from_user)
      
def createplayer(id):
    return{
        'id':id,
        'message':None,
        'sendresults':True
    }
        

def buildmenu(user, m=None):
    text='Выберите категорию для сборки:'
    kb=types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton(text='Роботы', callback_data='buildrobots'), types.InlineKeyboardButton(text='Танки', callback_data='buildtanks'))
    kb.add(types.InlineKeyboardButton(text='Турели', callback_data='buildturrets'), types.InlineKeyboardButton(text='Оружие', callback_data='buildweapons'))
    if m==None:
        bot.send_message(user.id, text, reply_markup=kb)
    else:
        medit(text, m.chat.id, m.message_id, reply_markup=kb)
         
@bot.message_handler(commands=['duel'])
def duel(m):
    kb=types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton(text='Вступить в бой', callback_data='battle join'))
    bot.send_message(m.chat.id, 'Набор игроков на дуэль!', reply_markup=kb)


    
@bot.callback_query_handler(func=lambda call:True)
def inline(call):
    user=users.find_one({'id':call.from_user.id})
    kb=types.InlineKeyboardMarkup()
    if 'build' in call.data:
        if 'robots' in call.data:
            spisok=robots
            name='робота'
        elif 'tanks' in call.data:
            spisok=tanks
            name='танк'
        elif 'turrets' in call.data:
            spisok=turrets
            name='турель'
        elif 'weapons' in call.data:
            spisok=weapons
            name='оружие'
        for ids in spisok:
            item=ids()
            kb.add(types.InlineKeyboardButton(text=item.name, callback_data='show '+item.type+' '+item.data))
        medit('Выберите '+name+' для просмотра:', call.message.chat.id, call.message.message_id, reply_markup=kb)
        
    if 'show' in call.data:
        medit('Выбрано: просмотр.', call.message.chat.id, call.message.message_id)
        data=call.data.split(' ')
        spisok=classes
        for ids in spisok:
            if data[2]==ids().data:
                item=ids()
        text=''
        text+='Название: '+item.name+'\n'
        text+='Тип: '+item.type+'\n'
        if item.type!='weapon':
            text+='ХП: '+str(item.hp)+'\n'
            text+='Скорость: '+str(item.speed)+'\n'
            text+='Занимает места: '+str(item.size)+'\n'
        text+='Цена (🔩): '+str(item.cost)+'\n'
        text+='Урон: '+str(item.damage)+'\n'
        bot.send_photo(call.message.chat.id, item.photo)
        kb=types.InlineKeyboardMarkup()
        kb.add(types.InlineKeyboardButton(text='Назад', callback_data='back'), types.InlineKeyboardButton(text='Собрать', callback_data='craft '+item.data))
        bot.send_message(call.message.chat.id, text, reply_markup=kb)
        
    if 'craft' in call.data:
        data=call.data.split(' ')[1]
        item=None
        for ids in classes:
            if ids().data==data:
                item=ids()
        if item!=None:
            cost=item.cost
            size=item.size
            myarmy=0
            for ids in user['army']:
                for idss in classes:
                    if idss.data==ids.data:
                        x=idss()
                myarmy+=x.size
            if user['iron']>=cost:
                if myarmy+item.size<=user['barracks']:
                    users.update_one({'id':user['id']},{'$inc':{'iron':-cost}})
                    users.update_one({'id':user['id']},{'$push':{'army':item.data}})
                    medit('Механизм "'+item.name+'" успешно собран!', call.message.chat.id, call.message.message_id, reply_markup=kb)
                else:
                    bot.answer_callback_query(call.id, 'Недостаточно места в бараках!')
            else:
                bot.answer_callback_query(call.id, 'Недостаточно железа!')
            
        
            
    
        
def createuser(user):
    return {
        'id':user.id,
        'name':user.first_name,
        'username':user.username,
        'army':[],
        'weapons':[],
        'money':100,
        'iron':400,
        'buildings':[],
        'barracks':20
    }
        
        
print('7777')
bot.polling(none_stop=True,timeout=600)


import os
import telebot
import time
import random
import threading
from telebot import types
from pymongo import MongoClient
import unit_classes
from tools import medit

token = os.environ['TELEGRAM_TOKEN']
bot = telebot.TeleBot(token)

allgames=0
games={}


class Game:
    
    def __init__(self):
        global allgames
        self.teams={}
        self.second=0
        self.users=[]
        self.started=False
        self.id=allgames
        games.update({allgames:self})
        allgames+=1
        
    def startgame(self):
        self.started=True
        for ids in self.teams:
            user=self.teams[ids]['player']
            if user['sendresults']!=False and user['id']!=None:
                try:
                    msg=bot.send_message(user['id'], 'Здесь будут отображаться результаты текущего боя.')
                    user['message']=msg
                except:
                    pass
        self.turn()
        
    def createteams(self, teams):
        x=0
        for ids in teams:
            self.teams.update({x:ids})
            for idss in self.teams[x]['army']: 
                self.teams[x]['army'][idss].teamid=x
            x+=1
        for ids in self.teams:
            for idss in self.teams[ids]['army']:
                unit=self.teams[ids]['army'][idss]
                print('Участник ['+str(unit.teamid)+']'+unit.name)
        
        
    def turn(self):
        self.second+=1
        if self.second%4==0:
            users=[]
            for ids in self.teams:
                user=self.teams[ids]['player']
                if user['sendresults']!=False and user['message']!=None and user['id']!=None:
                    pass # medit(результаты хп)
                    enemys=''
                    allies=''
                    for idss in self.teams:
                        team=self.teams[ids]
                        if team['player']['id']==user['id']:
                            x='ally'
                        else:
                            x='enemy'
                        for unit in team:
                            hp=round((unit['hp']/unit['maxhp'])*100, 1)
                            if x=='enemy':
                                emoj='🔴'
                                enemys+=emoj+'|'+unit.name+': ♥️'+str(hp)+'%\n'
                            else:
                                emoj='🔵'
                                allies+=emoj+'|'+unit.name+': ♥️'+str(hp)+'%\n'
                medit('Ситуация на поле боя:\n\n'+allies+'\n'+enemys, user.message.chat.id, user.message.message_id)
                            
                            
                        
        for ids in self.teams:
            team=self.teams[ids]
            for unit in team['army']:
                team['army'][unit].shootcd-=1
                
        for ids in self.teams:
            team=self.teams[ids]
            for unit in team['army']:
                if team['army'][unit].dead==False:
                    if team['army'][unit].shootcd<=0:
                        team['army'][unit].shoot(self.teams)
                        team['army'][unit].shootcd=team['army'][unit].shootspeed[1]
                    
        for ids in self.teams:
            team=self.teams[ids]
            for unit in team['army']:
                if team['army'][unit].hp<=0:
                    team['army'][unit].dead=True
        alive=[]
        for ids in self.teams:
            team=self.teams[ids]
            dead=0
            for unit in team['army']:
                if team['army'][unit].dead==True:
                    dead+=1
            if dead!=len(team):
                alive.append(team)
        if len(alive)<=1:
            self.endgame(alive)
        else:
            t=threading.Timer(1, self.turn)
            t.start()
        
    def endgame(self, alive):
        del games[self.id]
        bot.send_message(441399484, 'Игра завершена!')
            
        

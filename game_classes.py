import os
import telebot
import time
import random
import threading
from telebot import types
from pymongo import MongoClient
import unit_classes

games={}


class Game:
    
    def __init__(self):
        self.teams={}
        self.second=0
        self.started=False
        
    def startgame(self):
        self.started=True
        self.turn()
        
    def turn(self):
        self.second+=1
        for ids in self.teams:
            team=self.teams[ids]
            for unit in team:
                team[unit].shootcd-=1
                
        for ids in self.teams:
            team=self.teams[ids]
            for unit in team:
                if team[unit].dead==False:
                    if team[unit].shootcd<=0:
                        team[unit].shoot(self.teams)
                        team[unit].shootcd=team[unit].shootspeed[1]
                    
        for ids in self.teams:
            team=self.teams[ids]
            for unit in team:
                if unit.hp<=0:
                    unit.dead=True
        alive=[]
        for ids in self.teams:
            team=self.teams[ids]
            dead=0
            for unit in team:
                if unit.dead==True:
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
        print('Игра завершена!')
            
        

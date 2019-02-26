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
        for ids in self.teams:
            team=self.teams[ids]
            for unit in team:
                if team[unit].shootcd<=0:
                    team[unit].shoot()
                    team[unit].shootcd=team[unit].shootspeed[1]
            
        

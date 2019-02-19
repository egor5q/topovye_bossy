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


class Unit:
    
    def __init__(self):
        self.class=None  #tank/healer/damager/universal/summoner/buffer
        self.maxhp=1000
        self.maxattack=1000
        self.maxshield=1000
        self.skillmaxdmg=1000
        self.skillmaxdmg=1000
        self.maxsummons=0
        self.activebuffs=0
        self.activedebuffs=0
        self.passives=1
        self.attackskills=1
        self.actives=1
        self.dmgskills=1
        self.passivelist=[]
        self.activelist=[]


    
class Tank(Unit):
    
    def __init__(self):
        super().__init__()
        self.class='tank'
        self.maxhp=9000
        self.maxattack=1000
        self.maxshield=10000
        self.passives=3
        self.actives=6
        self.skillmaxdmg=2500
        
        
class Universal(Unit):
    
    def __init__(self):
        super().__init__()
        self.class='universal'
        self.maxhp=8500
        self.maxattack=3000
        self.maxshield=8500
        self.passives=2
        self.actives=7
        self.skillmaxdmg=5000
        
        
class Summoner(Unit):
    
    def __init__(self):
        super().__init__()
        self.class='summoner'
        self.maxhp=7000
        self.maxattack=2000
        self.maxshield=5000
        self.passives=3
        self.actives=8
        self.skillmaxdmg=0
        self.maxsummons=3
        
        
class Buffer(Unit):
    
    def __init__(self):
        super().__init__()  
        self.class='buffer'
        self.maxhp=7000
        self.maxattack=1000
        self.maxshield=8000
        self.passives=2
        self.actives=7
        self.activebuffs=4
        self.activedebuffs=3
        
        
class Attacker(Unit):
    
    def __init__(self):
        super().__init__()
        self.class='attacker'
        self.maxhp=6000
        self.maxattack=6000
        self.maxshield=6500
        self.passives=2
        self.actives=6
        self.skillmaxdmg=7000
        
        
    
class Healer(Unit):
    
    def __init__(self):
        super().__init__()
        self.class='healer'
        self.maxhp=7000
        self.maxattack=2000
        self.maxshield=4500
        self.passives=3
        self.actives=6
        self.attackskills=1
        self.skillmaxdmg=2500
        


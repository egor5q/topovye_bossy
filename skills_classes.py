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


class Skill:
    
    def __init__(self):
        self.effects={}  # Все типы, которые есть в скилле. Например: self.effects={'attack':{...}}
    
class Type:
    
    def __init__(self):
        self.targets='all'  # enemy/ally/all
        self.cost=1
        self.targets='all'
        self.dmg=0
        self.unit=None
        self.cd=1           # cooldown
    
    
class Effect:
    
    def __init__(self):
        self.type=None  # silence/reducedmg
        
    
class Attack(Type): 
    
    def __init__(self, dmg=0, targets='all', cd=1):
        super().__init__()
        self.targets=targets
        self.dmg=dmg
        self.cd=cd
        
        
class Summon(Type):
    
    def __init__(self, unit=units.Rock, cd=1):
        super().__init__()
        self.unit=unit
        self.cd=cd
        
        
class Heal(Type):
    
    def __init__(self, heal, targets='ally', cd=1):
        super().__init__()
        self.heal=heal
        self.targets=targets
        self.cd=cd
        
        
class Regenshield(Type):
    
    def __init__(self, regen, targets='ally', cd=1):
        super().__init__()
        self.regen=regen
        self.targets=targets
        self.cd=cd
        
        
class Debuff(Type):
    
    def __init__(self, effect, targets='enemy', cd=1):
        super().__init__()
        self.effect=effect
        self.targets=targets
        self.cd=cd
        
        
class Silence(Effect):
    
    def __init__(self):
        super().__init__()
        


    

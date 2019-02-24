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
        self.class=None  #tank/robot/human/turret


    
class Tank(Unit):
    
    def __init__(self):
        super().__init__()
        self.class='tank'

        
        
class Robot(Unit):
    
    def __init__(self):
        super().__init__()
        self.class='robot'

        
        
class Human(Unit):
    
    def __init__(self):
        super().__init__()
        self.class='human'

        
        
class Turret(Unit):
    
    def __init__(self):
        super().__init__()  
        self.class='turret'

        


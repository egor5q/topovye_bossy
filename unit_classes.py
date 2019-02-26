# -*- coding: utf-8 -*-
import os
import telebot
import time
import random
import threading
from telebot import types
from pymongo import MongoClient


token = os.environ['TELEGRAM_TOKEN']
bot = telebot.TeleBot(token)


#client=MongoClient(os.environ['database'])
#db=client.
#users=db.users
units=0

class Unit:
    
    def __init__(self):
        global units
        self.type=None  #tank/robot/human/turret
        self.shootspeed=[1, 5] # Сколько раз стреляет/Раз в сколько секунд (кд выстрела)
        self.size=1            # Сколько места в бараках занимает
        self.cost=400
        self.damage=150
        self.speed=100
        self.hp=500
        self.dead=False
        self.skills=[]
        self.shootcd=0
        self.photo='AgADAgAD0KoxG85oqEuj6f3E5jpHcBf-9A4ABEyPaiaRDjmUVzgFAAEC'
        self.id=units
        units+=1
        
    def shoot(self, teams):
        enemyteams=[]
        for ids in teams:
            if self not in teams[ids]:
                alive=0
                for idss in teams[ids]:
                    if teams[ids][idss].dead==False:
                        alive+=1
                if alive>0:
                    enemyteams.append(teams[ids])
        team=random.choice(enemyteams)
        enemies=[]
        for ids in team:
            if team[ids].dead==False:
                enemies.append(team[ids])
        enemy=random.choice(enemies)
        print('['+str(self.id)+']'+self.name+' стреляет в '+enemy.name+'!')
        x=0
        while x<self.shootspeed[0]:
            enemy.takeattack(self)
            x+=1
        
    def takeattack(self, enemy):
        self.hp-=enemy.damage
        print('['+str(self.id)+']'+self.name+' получает '+str(enemy.damage)+' урона! Осталось '+str(self.hp)+' хп.')
                
        
        
class Weapon:
    
    def __init__(self):
        self.type='weapon'
        self.shootspeed=[1, 3] # Сколько раз стреляет/Раз в сколько секунд (кд выстрела)
        self.cost=100
        self.damage=75
        self.photo='AgADAgAD0KoxG85oqEuj6f3E5jpHcBf-9A4ABEyPaiaRDjmUVzgFAAEC'

    
class Tank(Unit):
    
    def __init__(self):
        super().__init__()
        self.type='tank'

        
        
class Robot(Unit):
    
    def __init__(self):
        super().__init__()
        self.type='robot'

   

        
class Human(Unit):
    
    def __init__(self):
        super().__init__()
        self.type='human'

        
        
class Turret(Unit):
    
    def __init__(self):
        super().__init__()  
        self.type='turret'
        
        
class Test(Tank):
    
    def __init__(self):
        super().__init__()
        self.data='test'
        self.name='танк'
        self.damage=125
        self.speed=400
        self.cost=800
        self.hp=950
        self.shootspeed=[1, 8]
        self.photo='AgADAgADIqsxG_S_mEtSXlaP3lYsFAlsUw8ABCshaU23n-1NiYwAAgI'
        
class Test1(Robot):
    
    def __init__(self):
        super().__init__()
        self.data='test1'
        self.name='робот'
        self.shootspeed=[1, 4]
        self.photo='AgADAgADfqoxG8C9mUu53zMx4nEzjF52Uw8ABIgfsfgEkuMyWY4AAgI'
        
        
class Test2(Turret):
    
    def __init__(self):
        super().__init__()
        self.data='test2'
        self.name='турель'
        self.shootspeed=[3, 7]
        self.photo='AgADAgADKasxG_S_mEvGKrGBKHqqj6t3Uw8ABEXfZPnwvpCIJo4AAgI'
        
        
class Test3(Weapon):
    
    def __init__(self):
        super().__init__()
        self.data='test3'
        self.name='оружие'
        self.photo='AgADAgADKqsxG_S_mEurpfu42MBjZRSXOQ8ABCeg1E-5kdAMZ_MEAAEC'

        

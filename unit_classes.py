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
        self.photo='AgADAgAD0KoxG85oqEthzqWUuXJ6Vxf-9A4ABEyPaiaRDjmUVzgFAAEC'
        self.id=units
        self.ownerid=None
        units+=1
        
    def shoot(self, teams):
        enemyteams=[]
        for ids in teams:
            myteam=False
            for idss in teams[ids]['army']:
                unit=teams[ids]['army'][idss]
                if self.id==unit.id:
                    myteam=True
            if myteam==False:
                alive=0
                for idss in teams[ids]['army']:
                    if teams[ids]['army'][idss].dead==False:
                        alive+=1
                if alive>0:
                    enemyteams.append(teams[ids])
        team=random.choice(enemyteams)
        enemies=[]
        for ids in team['army']:
            if team['army'][ids].dead==False:
                enemies.append(team['army'][ids])
        enemy=random.choice(enemies)
        if self.shootspeed[0]==1:
            text='['+str(self.teamid)+']'+self.name+' стреляет в '+enemy.name+'!'
        else:
            text='['+str(self.teamid)+']'+self.name+' делает серию выстрелов по '+enemy.name+'!'
        print(text)
        x=0
        sumdmg=0
        while x<self.shootspeed[0]:
            dmg=enemy.takeattack(self)
            x+=1
            sumdmg+=dmg
        text='['+str(enemy.teamid)+']'+enemy.name+' получает '+str(sumdmg)+' урона! Осталось '+str(enemy.hp)+' хп.'
        
    def takeattack(self, enemy):
        dmg=enemy.damage
        self.hp-=dmg
        return dmg
                
        
        
class Weapon:
    
    def __init__(self):
        self.type='weapon'
        self.shootspeed=[1, 3] # Сколько раз стреляет/Раз в сколько секунд (кд выстрела)
        self.cost=100
        self.damage=75
        self.photo='AgADAgAD0KoxG85oqEthzqWUuXJ6Vxf-9A4ABEyPaiaRDjmUVzgFAAEC'

    
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
        self.speed=0
        
        
class Breaker(Tank):
    
    def __init__(self):
        super().__init__()
        self.data='breaker'
        self.name='Крушитель'
        self.damage=175
        self.speed=400
        self.cost=800
        self.hp=1150
        self.shootspeed=[1, 10]
        self.photo='AgADAgADIqsxG_S_mEtRkoWePaa75wlsUw8ABHCr3Ea3e9ddiIwAAgI'
        
class Lazerbot(Robot):
    
    def __init__(self):
        super().__init__()
        self.data='lazerbot'
        self.name='Лазербот-1150'
        self.damage=100
        self.hp=650
        self.shootspeed=[1, 6]
        self.photo='AgADAgADfqoxG8C9mUs6XyzO_r4jDF52Uw8ABIgfsfgEkuMyWY4AAgI'
        
        
class Multigun(Turret):
    
    def __init__(self):
        super().__init__()
        self.data='multigun'
        self.name='Multigun V-5'
        self.shootspeed=[3, 9]
        self.hp=400
        self.damage=75
        self.photo='AgADAgADKasxG_S_mEtLwhNFUY9sAAGrd1MPAARF32T58L6QiCaOAAIC'
        
        
class Test3(Weapon):
    
    def __init__(self):
        super().__init__()
        self.data='test3'
        self.name='оружие'
        self.photo='AgADAgADKqsxG_S_mEtKvjpgbffOQhSXOQ8ABCeg1E-5kdAMZ_MEAAEC'

        


import os
import telebot
import time
import random
import threading
from telebot import types
from pymongo import MongoClient
import unit_classes

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
        self.turn()
        
    def createteams(self, teams, users):
        x=0
        for ids in teams:
            self.teams.update({x:ids})
            for idss in self.teams[x]: 
                self.teams[x][idss].teamid=x
            x+=1
        for ids in self.teams:
            for idss in self.teams[ids]:
                unit=self.teams[ids][idss]
                print('Участник ['+str(unit.teamid)+']'+unit.name)
        self.users=users
        
    def turn(self):
        self.second+=1
        if self.second%5==0:
            users=[]
            for ids in self.players:
                if ids.sendresult!=False and ids.message!=None:
                    pass # medit(результаты хп)
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
                if team[unit].hp<=0:
                    team[unit].dead=True
        alive=[]
        for ids in self.teams:
            team=self.teams[ids]
            dead=0
            for unit in team:
                if team[unit].dead==True:
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
            
        

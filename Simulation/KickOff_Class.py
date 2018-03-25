# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 23:15:21 2018

@author: Lourenço Neto
"""

class Game:
    
    def __init__(self):
        self.timer = 0        
        self.field = [0]*68
        for i in range(68):
                self.field[i] = [0]*100
        self.ball_position = [50, 34]
        self.scores = [0, 0]
        
    
                
class Player:
    
    def __init__(self, player_data, position, group_player):
        self.data = player_data
        self.stamina = 100
        self.position = position
        self.name = player_data['name']
        self.group_player = group_player

    
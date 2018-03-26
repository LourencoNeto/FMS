# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 23:15:21 2018

@author: Lourenço Neto
"""
import random

class Game:
    
    def __init__(self):
        self.timer = 0        
        self.field = [0]*68
        for i in range(68):
                self.field[i] = [0]*100
        self.ball_position = [50, 34]
        self.scores = [0, 0]
        
    
    def rolling_game(self, home_team, away_team):
        if self.timer == 0:
            self.ball_position = home_team[10].position
        self.timer = self.timer + 1
        home_choice = []
        away_choice = []
        for player in home_team:
            home_choice.append(player.event_choice(self.ball_position))
        for player in away_team:
            away_choice.append(player.event_choice(self.ball_position))
        self.handle_event_choice(home_team, home_choice)
        return home_choice, away_choice
    
    def handle_event_choice(self, team, choices):
        i = 0
        
        for choice in choices:
            if team[i].group_player != "GoalKeeper":
                if choice == "Run":
                    rand_number = random.randint(0,3)
                    if rand_number == 0: #Run forward
                        new_position = team[i].position[0] + 6
                        if(new_position >= 100):
                            if(self.field[new_position][team[i].position[1]] != 0):
                                self.field[team[i].position[0]][team[i].position[1]] = 0 #The last positin is empty
                                team[i].position[0] = 98
                                self.field[team[i].position[0]][team[i].position[1]] = team[i] #The new position is filled with the player
                            else:
                                self.field[team[i].position[0]][team[i].position[1]] = 0 #The last positin is empty
                                team[i].position[0] = 99
                                self.field[team[i].position[0]][team[i].position[1]] = team[i] #The new position is filled with the player
                        else: 
                            if(self.field[new_position][team[i].position[1]] != 0):
                                self.field[team[i].position[0]][team[i].position[1]] = 0 #The last positin is empty
                                team[i].position[0] = team[i].position[0] + 5
                                self.field[team[i].position[0]][team[i].position[1]] = team[i] #The new position is filled with the player
                            
                            else:
                                self.field[team[i].position[0]][team[i].position[1]] = 0 #The last positin is empty
                                team[i].position[0] = team[i].position[0] + 6
                                self.field[team[i].position[0]][team[i].position[1]] = team[i] #The new position is filled with the player
      
                    elif rand_number == 1: #Run to the left
                        new_position = team[i].position[1] - 6
                        if(new_position < 0):
                            if(self.field[team[i].position[0]][new_position] != 0):
                                self.field[team[i].position[0]][team[i].position[1]] = 0 #The last positin is empty
                                team[i].position[1] = 1
                                self.field[team[i].position[0]][team[i].position[1]] = team[i] #The new position is filled with the player
                            
                            else:
                                self.field[team[i].position[0]][team[i].position[1]] = 0 #The last positin is empty
                                team[i].position[1] = 0
                                self.field[team[i].position[0]][team[i].position[1]] = team[i] #The new position is filled with the player

                        else: 
                        
                            if(self.field[team[i].position[0]][new_position] != 0):
                            
                                self.field[team[i].position[0]][team[i].position[1]] = 0 #The last positin is empty
                                team[i].position[1] = team[i].position[1] - 5
                                self.field[team[i].position[0]][team[i].position[1]] = team[i] #The new position is filled with the player
                           
                            else:
                                self.field[team[i].position[0]][team[i].position[1]] = 0 #The last positin is empty
                                team[i].position[1] = team[i].position[1] - 6
                                self.field[team[i].position[0]][team[i].position[1]] = team[i] #The new position is filled with the player

                    elif rand_number == 2: #Run backward
                        new_position = team[i].position[0] - 6
                        if(new_position < 0):
                            if(self.field[new_position][team[i].position[0]] != 0):
                                self.field[team[i].position[0]][team[i].position[1]] = 0 #The last positin is empty
                                team[i].position[0] = 1
                                self.field[team[i].position[0]][team[i].position[1]] = team[i] #The new position is filled with the player

                            else:
                                self.field[team[i].position[0]][team[i].position[1]] = 0 #The last positin is empty
                                team[i].position[0] = 0
                                self.field[team[i].position[0]][team[i].position[1]] = team[i] #The new position is filled with the player

                        else: 
                        
                            if(self.field[new_position][team[choices.index(choice)].position[0]] != 0):
                                self.field[team[i].position[0]][team[i].position[1]] = 0 #The last positin is empty
                                team[i].position[0] = team[i].position[0] - 5
                                self.field[team[i].position[0]][team[i].position[1]] = team[i] #The new position is filled with the player

                            else:
                                self.field[team[i].position[0]][team[i].position[1]] = 0 #The last positin is empty
                                team[i].position[0] = team[i].position[0] - 6
                                self.field[team[i].position[0]][team[i].position[1]] = team[i] #The new position is filled with the player

                    elif rand_number == 3: #Run to the right
                        new_position = team[i].position[1] + 6
                        if(new_position >= 68):
                            if(self.field[team[i].position[0]][new_position] != 0):
                                self.field[team[i].position[0]][team[i].position[1]] = 0 #The last positin is empty
                                team[i].position[1] = 66
                                self.field[team[i].position[0]][team[i].position[1]] = team[i] #The new position is filled with the player

                            else:
                                self.field[team[i].position[0]][team[i].position[1]] = 0 #The last positin is empty
                                team[i].position[1] = 67
                                self.field[team[i].position[0]][team[i].position[1]] = team[i] #The new position is filled with the player

                        else: 
                        
                            if(self.field[team[i].position[0]][new_position] != 0):
                                self.field[team[i].position[0]][team[i].position[1]] = 0 #The last positin is empty
                                team[i].position[1] = team[i].position[1] + 5
                                self.field[team[i].position[0]][team[i].position[1]] = team[i] #The new position is filled with the player

                            else:
                                self.field[team[i].position[0]][team[i].position[1]] = 0 #The last positin is empty
                                team[i].position[1] = team[i].position[1] + 6
                                self.field[team[i].position[0]][team[i].position[1]] = team[i] #The new position is filled with the player
          
                elif choice == "Pass":
                    print("Pass")
                elif choice == "Shoot":
                    print("Shoot")
            i = i + 1

class Player:
    
    def __init__(self, player_data, position, group_player, field_owner):
        self.data = player_data
        self.stamina = 100
        self.position = position
        self.name = player_data['name']
        self.group_player = group_player
        self.field_owner = field_owner

    def event_choice(self, ball_position):
        choice = []
        #print(self.name)
        if ball_position == self.position: #The player with the ball
            rand_number = random.randint(0,100)
            print(rand_number, self.name)    
            if self.field_owner == "Home" and self.position[1] >= 100 - 28: #The player is a member of the home team and he/she is the defense area of the enemy
                
                if rand_number >= 40: #This will indicate that the player will shoot
                    choice = "Shoot"
                elif rand_number >= 20 and rand_number < 40: #This will indicate that the player will pass
                    choice = "Pass"
                else: #This will indicate that the player will run
                    choice = "Run"
                    
            elif self.field_owner == "Away" and self.position[1] <= 28: #The player is a member of the away team and he/she is the defense area of the enemy
                
                if rand_number >= 40: #This will indicate that the player will shoot
                    choice = "Shoot"
                elif rand_number >= 20 and rand_number < 40: #This will indicate that the player will pass
                    choice = "Pass"
                else: #This will indicate that the player will run
                    choice = "Run"
                
            else: #The player is not on conditions to shoot
            
                if rand_number >= 50: #This will indicate that the player should pass
                    choice = "Pass"
                else: #This will indicate that the player should run
                    choice = "Run"
                    
        else: #The ball is not with the player
            choice = "Run"
        
        return choice
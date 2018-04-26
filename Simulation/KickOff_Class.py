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
        #self.ball_position = [50, 34]
        self.scores = [0, 0]
        self.ball_owner = [-1, 1]
    
    def rolling_game(self, home_team, away_team):
        self.home_team = home_team
        self.away_team = away_team
        if self.timer == 0:
            self.ball_position = home_team[10].position
            self.ball_owner = [1, 10] #Home Team represents 1, Away Team represents 2 and the other represents the number order of the player
        self.timer = self.timer + 1
        home_choice = []
        away_choice = []
        for player_home in home_team:
            home_choice.append(player_home.event_choice(self.ball_owner))
        for player_away in away_team:
            away_choice.append(player_away.event_choice(self.ball_owner))
        "Stactly saving the previous score (If we only set the variable to another, it will be like a pointer"
        previous_score = []
        previous_score.append(self.scores[0])
        previous_score.append(self.scores[1])
        self.handle_event_choice(home_team, home_choice)
        self.handle_event_choice(away_team, away_choice)
        actual_score = self.scores
        if previous_score != actual_score:
            scorer = -1
            if previous_score[0] != actual_score[0]: #Goal from the Home Team
                scorer = 0
            elif previous_score[1] != actual_score[1]: #Goal from the Away Team
                scorer = 1
            self.original_field_formation(home_team, away_team, scorer)
    
    def handle_event_choice(self, team, choices):
        i = 0
        for choice in choices:
            if team[i].group_player != "GoalKeeper":
                if choice == "Run":
                    rand_numb = random.randint(0,3)
                    previous_position = team[i].position
                    self.field[previous_position[0]][previous_position[1]] = 0
                    new_position = previous_position
                    if rand_numb == 0: #Moving Forward
                        
                        if [2, i] != self.ball_owner: #If the player is roling the ball, than it can't move backward
                            new_position[1] = new_position[1] + 4
                            if(new_position[1] >= 100):
                                new_position[1] = 99
                            if(self.field[new_position[0]][new_position[1]] != 0): #There is somebody at the position
                                new_position[1] = new_position[1] - 1
                        else:                       
                            self.aux(team[i], choice)
                    elif rand_numb == 1: #Moving to the Left
                        
                        new_position[0] = new_position[0] - 4
                        if(new_position[0] < 0):
                            new_position[0] = 0
                        if(self.field[new_position[0]][new_position[1]] != 0):
                            new_position[0] = new_position[0] + 1
                        
                    elif rand_numb == 2: #Moving Backward

                        if [1, i] != self.ball_owner: #If the player is roling the ball, than it can't move backward
                            new_position[1] = new_position[1] - 4
                            if(new_position[0] < 0):
                                new_position[0] = 0
                            if(self.field[new_position[0]][new_position[1]] != 0):
                                new_position[1] = new_position[1] + 1
                        else:                           
                            self.aux(team[i], choice)
                    elif rand_numb == 3: #Moving to the Right
                        
                        new_position[0] = new_position[0] + 4
                        if(new_position[0] >= 68):
                            new_position[0] = 67
                        if(self.field[new_position[0]][new_position[1]] != 0):
                            new_position[1] = new_position[1] - 1
                        
                    self.field[new_position[0]][new_position[1]] = team[i]                   
                    team[i].position = new_position
                elif choice == "Pass":
                    #print(team[i].field_owner)
                    order_formation_player_receive_ball = self.found_the_closest_player(team, team[i])
                    representation = -1
                    if team[i].field_owner == "Home":
                        representation = 1
                    elif team[i].field_owner == "Away":
                        representation = 2
                        
                    self.ball_owner = [representation, order_formation_player_receive_ball]
                elif choice == "Shoot":
                    #print(team[i].group_player)
                    
                    finishing = team[i].data["finishing"]
                    shot_power = team[i].data["shot_power"]
                    gk_handling = team[i].data["gk_handling"]
                    distance = 0
                    if team[i].field_owner == "Home":
                        distance = self.distance_measure(team[i], self.away_team[0])
                    elif team[i].field_owner == "Away":
                        distance = self.distance_measure(team[i], self.home_team[0])
                    formula = (finishing*shot_power)/(distance*gk_handling)
                    #print(team[i].position, self.away_team[0].position, distance)
                    #print(formula, team[i].position, team[i].field_owner)
                    #if(formula > 0.3 and team[i].field_owner == "Home"):
                    if(team[i].field_owner == "Home"):
                        if(formula > 0.6):
                            self.scores[0] = self.scores[0] + 1
                            team[i].goals = team[i].goals + 1
                        else:
                            self.ball_owner = [2, 0] #Ball will be with the goalkeeper from the other team
                    elif(team[i].field_owner == "Away"):
                        if(formula > 0.6):
                            self.scores[1] = self.scores[1] + 1
                            team[i].goals = team[i].goals + 1
                        else:
                            self.ball_owner = [1, 0] #Ball will be with the goalkeeper from the other team
            else: #Now, let's analyze the goalkeeper
                representation = -1
                if team[i].field_owner == "Home":
                    representation = 1
                elif team[i].field_owner == "Away":
                    representation = 2
                if self.ball_owner == [representation, 0]: #The GoalKeeper has the ball
                    order_formation_player_receive_ball = self.found_the_closest_player(team, team[i])
                    self.ball_owner = [representation, order_formation_player_receive_ball]
            i = i + 1
            
    def aux(self, player, choice):
        "This function is responsible to help the handle_event_choice method to not let the player with the ball run to its goalkeeper"
        aux_player = []
        aux_choice = []
        aux_player.append(player)
        aux_choice.append(choice)
        self.handle_event_choice(aux_player, aux_choice)
        
    def distance_measure(self, player_1, player_2):
        dist_y = player_1.position[1] - player_2.position[1]
        dist_x = player_1.position[0] - player_2.position[0]
        distance = dist_y*dist_y + dist_x*dist_x
        return distance
    
    def original_field_formation(self, home_team, away_team, scorer):
        "Set the field to be total empty"
        
        for i in range(68):
            for j in range(100):
                self.field[i][j] = 0
        
        "Then, fill it with the players"
        for player in home_team:
            ofp = []
            ofp.append(player.original_formation_position[0])
            ofp.append(player.original_formation_position[1])
            self.field[player.original_formation_position[0]][player.original_formation_position[1]] = player
            player.position[0] = ofp[0]
            player.position[1] = ofp[1]
        for player in away_team:
            ofp = []
            ofp.append(player.original_formation_position[0])
            ofp.append(player.original_formation_position[1])
            self.field[player.original_formation_position[0]][player.original_formation_position[1]] = player
            player.position[0] = ofp[0]
            player.position[1] = ofp[1]
        
        if scorer == 0:
            self.ball_owner = [2, 10]
        elif scorer == 1:
            self.ball_owner = [1, 10]
            
    def found_the_closest_player(self, team, player_with_ball):
        min_distance = 14624 #Distance between 2 opposite corners
        player_to_receive_order = -1
        player_to_receive_real_order = -1
        for free_player in team:
            
            if free_player.position != player_with_ball.position:
                distance_fp_pwb = self.distance_measure(free_player, player_with_ball)
                if distance_fp_pwb < min_distance:
                    
                    min_distance = distance_fp_pwb
                    player_to_receive_order = free_player.team_queue
                    if free_player.position[1] > player_with_ball.position[1] and free_player.field_owner == "Home":
                        player_to_receive_real_order = free_player.team_queue
                    if free_player.position[1] < player_with_ball.position[1] and free_player.field_owner == "Away":
                        player_to_receive_real_order = free_player.team_queue
        if player_to_receive_real_order == -1:         
            return player_to_receive_order
        else:
            return player_to_receive_real_order
        

class Player:
    
    def __init__(self, player_data, position, group_player, field_owner, team_queue):
        self.data = player_data
        self.stamina = 100
        self.position = position
        self.name = player_data['name']
        self.group_player = group_player
        self.field_owner = field_owner
        self.team_queue = team_queue
        
        self.original_formation_position = []
        self.original_formation_position.append(position[0])
        self.original_formation_position.append(position[1])
        self.goals = 0
        #self.rand = -1
        #self.choice = ""

    def event_choice(self, ball_owner):
        choice = []
        #print(self.name)
        representation = -1
        if self.field_owner == "Home":
            representation = 1
        elif self.field_owner == "Away":
            representation = 2
        if ball_owner == [representation, self.team_queue]: #The player with the ball
            rand_number = random.randint(0,100)
            self.rand = rand_number
            #print(rand_number)  
            if self.field_owner == "Home" and self.position[1] >= 100 - 28: #The player is a member of the home team and he/she is the defense area of the enemy
                
                if rand_number >= 20: #This will indicate that the player will shoot
                    choice = "Shoot"
                elif rand_number >= 10 and rand_number < 20: #This will indicate that the player will pass
                    choice = "Pass"
                else: #This will indicate that the player will run
                    choice = "Run"
                    
            elif self.field_owner == "Away" and self.position[1] <= 28: #The player is a member of the away team and he/she is the defense area of the enemy
                
                if rand_number >= 20: #This will indicate that the player will shoot
                    choice = "Shoot"
                elif rand_number >= 10 and rand_number < 20: #This will indicate that the player will pass
                    choice = "Pass"
                else: #This will indicate that the player will run
                    choice = "Run"
                
            else: #The player is not on conditions to shoot
            
                if rand_number >= 80: #This will indicate that the player should pass
                    choice = "Pass"
                else: #This will indicate that the player should run
                    choice = "Run"
            
            if self.group_player == "GoalKeeper": #Pick it up the ball after a missing shot
                choice = "Pass"
        else: #The ball is not with the player
            choice = "Run"
        self.choice = choice
        return choice
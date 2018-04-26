# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 17:19:47 2018

@author: Lourenço Neto
"""

def Teste():
    
    boolean = False
    formation = 442
    return boolean, formation

def Grouping_By_Position(team_players, group):
    positions = []
    group_players = []
    
    if group == "Forward":
        positions = ["cf", "lw", "rw", "st", "lf", "rf", "rs", "ls"]
    elif group == "MidField":
        positions = ["cm", "rm", "lm", "cam", "cdm", "rdm", "ldm", "ram", "lam", "rwb", "lwb", "rcm", "lcm"]
    elif group == "Defender":
        positions = ["lb", "cb", "rb", "rcb", "lcb"]
    else:
        positions = ["gk"]
    for i in range(len(positions)):
        positions[i] = "prefers_" + positions[i]
    
    for index, player in team_players.iterrows():
        count = 0
        for label in positions:
            if player[label] == True and count == 0:
                group_players.append(player)
                count = count + 1
    return group_players

def Filling_Field(kickoff, home_starting_team, away_starting_team, formation):
    "We need the list of the players in the field"
    HomeTeam = []
    AwayTeam = []
    
    "GoalKeepers"
    kickoff.field[33][2] = kc.Player(home_starting_team[0], [33, 2], "GoalKeeper", "Home", 0)
    HomeTeam.append(kickoff.field[33][2])
    
    kickoff.field[33][100 - 2] = kc.Player(away_starting_team[0], [33, 100 - 2], "GoalKeeper", "Away", 0)
    AwayTeam.append(kickoff.field[33][100 - 2])
        
    "Center Back Defenders"
    
    kickoff.field[24][100 - 26] = kc.Player(away_starting_team[1], [24, 100 - 26], "Defender", "Away", 1)
    AwayTeam.append(kickoff.field[24][100 - 26])
    
    kickoff.field[68 - 24][100 - 26] = kc.Player(away_starting_team[2], [68 - 24, 100 - 26], "Defender", "Away", 2)
    AwayTeam.append(kickoff.field[68 - 24][100 - 26])
    
    "Now, let's analyze how many center back will play at the home team and put in the field"
    number_defenders = formation / 100
    number_defenders = int(number_defenders)
    if number_defenders == 3: # 1 center back
        kickoff.field[34][28] = kc.Player(home_starting_team[1], [34, 28], "Defender", "Home", 1)
        HomeTeam.append(kickoff.field[34][28])
    
    else: # 2 or 3 center backs
        
        kickoff.field[24][26] = kc.Player(home_starting_team[1], [24, 26], "Defender", "Home", 1)
        HomeTeam.append(kickoff.field[24][26])
        
        kickoff.field[68 - 24][26] = kc.Player(home_starting_team[2], [68 - 24, 26], "Defender", "Home", 2)
        HomeTeam.append(kickoff.field[68 - 24][26])
        
        if number_defenders == 5: # 3 center backs
            kickoff.field[34][28] = kc.Player(home_starting_team[3], [34, 28], "Defender", "Home", 3)
            HomeTeam.append(kickoff.field[34][28])

    "Let's analyze if the formation have 3 defenders (If it does, the defense should be more dense and the position of the left and right backs gonna change)"
    
    delta_vector_position = 0
    delta_back_x = 0
    if number_defenders == 3:
        delta_back_x = 5
        delta_vector_position = 1
    elif number_defenders == 5:
        delta_vector_position = -1
    
    "Left Back Defenders"
    
    kickoff.field[12 + delta_back_x][28] = kc.Player(home_starting_team[3 - delta_vector_position], [12 + delta_back_x, 28], "Defender", "Home", 3 - delta_vector_position)
    HomeTeam.append(kickoff.field[12 + delta_back_x][28])

    kickoff.field[68 - 12][100 - 28] = kc.Player(away_starting_team[3], [68 - 12, 100 - 28], "Defender", "Away", 3)
    AwayTeam.append(kickoff.field[68 - 12][100 - 28])
        
    "Right Back Defenders"
    kickoff.field[68 - 12 - delta_back_x][28] = kc.Player(home_starting_team[4 - delta_vector_position], [68 - 12 - delta_back_x, 28], "Defender", "Home", 4 - delta_vector_position)
    HomeTeam.append(kickoff.field[68 - 12 - delta_back_x][28])
    
    kickoff.field[12][100 - 28] = kc.Player(away_starting_team[4], [12, 100 - 28], "Defender", "Away", 4)
    AwayTeam.append(kickoff.field[12][100 - 28])
    
    team_queue_position_last_defender = 4 - delta_vector_position # Necessary to inform the positions at the queue of the next players
    
    "Middfields"            
    
    kickoff.field[24][100 - 38] = kc.Player(away_starting_team[5], [24, 100 - 38], "MidField", "Away", 5)
    AwayTeam.append(kickoff.field[24][100 - 38])
        
    kickoff.field[68 - 24][100 -38] = kc.Player(away_starting_team[6], [68 - 24, 100 - 38], "MidField", "Away", 6)
    AwayTeam.append(kickoff.field[68 - 24][100 - 38])
    
    "Now let's analyze how many midfields will play for the manager team according to its formation"
    aux = formation % 100
    number_midfields = aux / 10
    number_midfields = int(number_midfields)
    
    team_queue_position_last_mid_not_side = team_queue_position_last_defender
    if number_midfields == 3: # Only 1 player not positioned at the side of the field
        kickoff.field[34][40] = kc.Player(home_starting_team[team_queue_position_last_defender + 1], [34, 40], "MidField", "Home", team_queue_position_last_defender + 1)
        HomeTeam.append(kickoff.field[34][40])
        team_queue_position_last_mid_not_side += 1
    else: # 2 or 3 players not positioned at the side of the field
        kickoff.field[24][38] = kc.Player(home_starting_team[team_queue_position_last_defender + 1], [24, 38], "MidField", "Home", team_queue_position_last_defender + 1)
        HomeTeam.append(kickoff.field[24][38])
    
        kickoff.field[68 - 24][38] = kc.Player(home_starting_team[team_queue_position_last_defender + 2], [68 - 24, 38], "MidField", "Home", team_queue_position_last_defender + 2)
        HomeTeam.append(kickoff.field[68 - 24][38])
        
        team_queue_position_last_mid_not_side += 2
        if number_midfields == 5:
            kickoff.field[34][40] = kc.Player(home_starting_team[team_queue_position_last_defender + 3], [34, 40], "MidField", "Home", team_queue_position_last_defender + 3)
            HomeTeam.append(kickoff.field[34][40])
            team_queue_position_last_mid_not_side += 1
    "Let's check if the number of midfields is 3. If it is, then we should put a denser formation"
    
    delta_mid_x = 0
    if number_midfields == 3:
        delta_mid_x = 5
    
    "Left Midfields"
    
    kickoff.field[12 + delta_mid_x][40] = kc.Player(home_starting_team[team_queue_position_last_mid_not_side + 1], [12 + delta_mid_x, 40], "Defender", "Home", team_queue_position_last_mid_not_side + 1)
    HomeTeam.append(kickoff.field[12 + delta_mid_x][40])
    
    kickoff.field[68 - 12][100 - 38] = kc.Player(away_starting_team[7], [68 - 12, 100 - 38], "MidField", "Away", 7)
    AwayTeam.append(kickoff.field[68 - 12][100 - 38])
    
    "Right Midfields"
    
    kickoff.field[68 - 12 - delta_mid_x][40] = kc.Player(home_starting_team[team_queue_position_last_mid_not_side + 2], [68 - 12 - delta_mid_x, 40], "Defender", "Home", team_queue_position_last_mid_not_side + 2)
    HomeTeam.append(kickoff.field[68 - 12 - delta_mid_x][40])
    
    kickoff.field[12][100 - 38] = kc.Player(away_starting_team[8], [12, 100 - 38], "MidField", "Away", 8)
    AwayTeam.append(kickoff.field[12][100 - 38])
    
    team_queue_position_last_mid = team_queue_position_last_defender + number_midfields
    
    "Forwards"
    "Let's check how many forwards the manager team will not have at the side of field"
    number_forwards = aux % 10   
    delta_forward_x = 0
    
    team_queue_position_last_forward_not_side = team_queue_position_last_mid
    if number_forwards == 3: # Then, exist a forward, probably a striker, at the field
        delta_forward_x = -7        
        kickoff.field[34][48] = kc.Player(home_starting_team[team_queue_position_last_mid + 1], [34, 48], "MidField", "Home", team_queue_position_last_mid + 1)
        HomeTeam.append(kickoff.field[34][48])
        team_queue_position_last_forward_not_side += 1
           
    "Left Forward"
        
    kickoff.field[24 + delta_forward_x][48] = kc.Player(home_starting_team[9], [24 + delta_forward_x, 48], "Forward", "Home", 9)
    HomeTeam.append(kickoff.field[24 + delta_forward_x][48])
    
    kickoff.field[68 - 24 - delta_forward_x][100 - 48] = kc.Player(away_starting_team[9], [68 - 24 - delta_forward_x, 100 - 48], "Forward", "Away", 9)
    AwayTeam.append(kickoff.field[68 - 24 - delta_forward_x][100 - 48])
    
    "Right Forward"

    kickoff.field[68 - 24][48] = kc.Player(home_starting_team[10], [68 - 24, 48], "Forward", "Home", 10)
    HomeTeam.append(kickoff.field[68 - 24][48])
        
    kickoff.field[24][100 - 48] = kc.Player(away_starting_team[10], [24, 100 - 48], "Forward", "Away", 10)
    AwayTeam.append(kickoff.field[24][100 - 48])
    
    return kickoff.field, HomeTeam, AwayTeam

import KickOff_Class as kc

# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 17:19:47 2018

@author: Lourenço Neto
"""


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

def Filling_Field(kickoff, home_starting_team, away_starting_team):
    "We need the list of the players in the field"
    HomeTeam = []
    AwayTeam = []
    
    
    "GoalKeepers"
    kickoff.field[33][2] = kc.Player(home_starting_team[0], [33, 2], "GoalKeeper", "Home")
    HomeTeam.append(kickoff.field[33][2])
    
    kickoff.field[33][100 - 2] = kc.Player(away_starting_team[0], [33, 100 - 2], "GoalKeeper", "Away")
    AwayTeam.append(kickoff.field[33][100 - 2])

    "Defenders"
    kickoff.field[24][26] = kc.Player(home_starting_team[1][0], [24, 26], "Defender", "Home")
    HomeTeam.append(kickoff.field[24][26])
    
    kickoff.field[24][100 - 26] = kc.Player(away_starting_team[1][0], [24, 100 - 26], "Defender", "Away")
    AwayTeam.append(kickoff.field[24][100 - 26])
    
    kickoff.field[68 - 24][26] = kc.Player(home_starting_team[1][1], [68 - 24, 26], "Defender", "Home")
    HomeTeam.append(kickoff.field[68 - 24][26])
    
    kickoff.field[68 - 24][100 - 26] = kc.Player(away_starting_team[1][1], [68 - 24, 100 - 26], "Defender", "Away")
    AwayTeam.append(kickoff.field[68 - 24][100 - 26])
    
    kickoff.field[12][28] = kc.Player(home_starting_team[1][2], [12, 28], "Defender", "Home")
    HomeTeam.append(kickoff.field[12][28])
    
    kickoff.field[12][100 - 28] = kc.Player(away_starting_team[1][2], [12, 100 - 28], "Defender", "Away")
    AwayTeam.append(kickoff.field[12][100 - 28])
    
    kickoff.field[68 - 12][28] = kc.Player(home_starting_team[1][3], [68 - 12, 28], "Defender", "Home")
    HomeTeam.append(kickoff.field[68 - 12][28])
    
    kickoff.field[68 - 12][100 - 28] = kc.Player(away_starting_team[1][3], [68 - 12, 100 - 28], "Defender", "Away")
    AwayTeam.append(kickoff.field[68 - 12][100 - 28])
     
    "MidFields"
    kickoff.field[12][40] = kc.Player(home_starting_team[2][0], [12, 40], "MidField", "Home")
    HomeTeam.append(kickoff.field[12][40])
    
    kickoff.field[12][100 - 40] = kc.Player(away_starting_team[2][0], [12, 100 - 40], "MidField", "Away")
    AwayTeam.append(kickoff.field[12][100 - 40])
    
    kickoff.field[24][40] = kc.Player(home_starting_team[2][1], [24, 40], "MidField", "Home")
    HomeTeam.append(kickoff.field[24][40])
    
    kickoff.field[24][100 - 40] = kc.Player(away_starting_team[2][1], [24, 100 - 40], "MidField", "Away")
    AwayTeam.append(kickoff.field[24][100 - 40])
    
    kickoff.field[68 - 24][40] = kc.Player(home_starting_team[2][2], [68 - 24, 40], "MidField", "Home")
    HomeTeam.append(kickoff.field[68 - 24][40])
    
    kickoff.field[68 - 24][100 -40] = kc.Player(away_starting_team[2][2], [68 - 24, 100 - 40], "MidField", "Away")
    AwayTeam.append(kickoff.field[68 - 24][100 - 40])
    
    kickoff.field[68 - 12][40] = kc.Player(home_starting_team[2][3], [68 - 12, 40], "MidField", "Home")
    HomeTeam.append(kickoff.field[68 - 12][40])
    
    kickoff.field[68 - 12][100 - 40] = kc.Player(away_starting_team[2][3], [68 - 12, 100 - 40], "MidField", "Away")
    AwayTeam.append(kickoff.field[68 - 12][100 - 40])
    
    "Forwards"
    kickoff.field[24][48] = kc.Player(home_starting_team[3][0], [24, 48], "Forward", "Home")
    HomeTeam.append(kickoff.field[24][48])
    
    kickoff.field[24][100 - 48] = kc.Player(away_starting_team[3][0], [24, 100 - 48], "Forward", "Away")
    AwayTeam.append(kickoff.field[24][100 - 48])
    
    kickoff.field[68 - 24][48] = kc.Player(home_starting_team[3][1], [68 - 24, 48], "Forward", "Home")
    HomeTeam.append(kickoff.field[68 - 24][48])
    
    kickoff.field[68 - 24][100 - 48] = kc.Player(away_starting_team[3][1], [68 - 24, 100 - 48], "Forward", "Away")
    AwayTeam.append(kickoff.field[68 - 24][100 - 48])
    
    return kickoff.field, HomeTeam, AwayTeam

import pandas as pd
import KickOff_Class as kc

"Reading the FIFA 18 database from the Database Folder"
database = pd.read_csv('Database/FIFA18_database.csv')

"Picking the teams from the Premier League"
premier_league = database.loc[database.league == 'English Premier League']
english_teams = premier_league.club.unique().tolist()

"Choosing the Home and Away Teams (In this step of the development, we are just checking the model)"
"After the model being tested, one of the Teams will be from the user and the other, its opponent"
Home_Team = database.loc[database.club == english_teams[0]]
Away_Team = database.loc[database.club == english_teams[1]]

"Choosing the Formation (Like the previous part, in this step, the chosen formation will be 4-2-2, only for the purpose of test)"
"And scaling the Starting Team"
   
Forward_Home_Players = Grouping_By_Position(Home_Team, "Forward")[:2]
Forward_Away_Players = Grouping_By_Position(Away_Team, "Forward")[:2]
MidField_Home_Players = Grouping_By_Position(Home_Team, "MidField")[:4]
MidField_Away_Players = Grouping_By_Position(Away_Team, "MidField")[:4]
Defender_Home_Players = Grouping_By_Position(Home_Team, "Defender")[:4]
Defender_Away_Players = Grouping_By_Position(Away_Team, "Defender")[:4]
GoalKeeper_Home_Player = Grouping_By_Position(Home_Team, "GoalKeeper")[0]
GoalKeeper_Away_Player = Grouping_By_Position(Away_Team, "GoalKeeper")[0]

Home_Starting_Team = list([GoalKeeper_Home_Player, Defender_Home_Players, MidField_Home_Players, Forward_Home_Players])
Away_Starting_Team = list([GoalKeeper_Away_Player, Defender_Away_Players, MidField_Away_Players, Forward_Away_Players])

"Filling the field with the players before the beginning of the game"
Kick_off = kc.Game()
Kick_off.field, Home_PlayingTeam, Away_PlayingTeam = Filling_Field(Kick_off, Home_Starting_Team, Away_Starting_Team)
field = Kick_off.field
print(len(Home_PlayingTeam), Home_PlayingTeam[0].name, len(Away_PlayingTeam), Away_PlayingTeam[0].name)
hc = []
ac = []
"Rolling the game"
while Kick_off.timer <= 1:
    hc, ac = Kick_off.rolling_game(Home_PlayingTeam, Away_PlayingTeam)
    field = Kick_off.field





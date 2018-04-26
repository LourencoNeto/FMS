from SimulatorModules import ManagerTeam
from menu import *
from selection_menu import *
from manager_menu import *
from game_menu import *

pygame.init()
name, quit = menu()
if not quit:
    team, quit = selection_menu()
if not quit:
    opponents = OpponentsOrder(team)
    number = 0
    Away_Team = opponents.get_opponent(number)
    away = opponents.get_opponent_name(number)
    Manager_Team, quit = manager_menu(name, team, away)
while not quit:
    quit = game_menu(team, away, Manager_Team, Away_Team)
    number += 1
    if number > 18:
        number = 0
    Away_Team = opponents.get_opponent(number)
    away = opponents.get_opponent_name(number)
    if not quit:
        Manager_Team, quit = manager_menu(name, team, away, Manager_Team)
pygame.quit()

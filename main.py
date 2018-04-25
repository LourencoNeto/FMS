from SimulatorModules import ManagerTeam
from menu import *
from selection_menu import *
from manager_menu import *

name, quit = menu()
if not quit:
    team, quit = selection_menu()
if not quit:
    manager_menu(name, team)

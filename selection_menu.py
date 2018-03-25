import pygame
from SimulatorModules import *
import pandas as pd

pygame.init()
surface_height = 550
surface_width = 240
main_surface = pygame.display.set_mode((surface_width, surface_height))
font = pygame.font.SysFont(None, 20)
clock = pygame.time.Clock()

database = pd.read_csv('Simulation/Database/FIFA18_database.csv')
premier_league = database.loc[database.league == 'English Premier League']
english_teams = premier_league.club.unique().tolist()
box_list = []
y = 40
for name in english_teams:
    Box = SelectBox(40, y, 170, name)
    box_list.append(Box)
    y += 20
Next_Button = Button(130, 500, 100, 40, 40, 13, "Next")
main_surface.fill((33, 94, 33))
main_surface.blit(font.render("Selecione seu time:", True, pygame.Color("black")), (10, 10))
Next_Button.draw(main_surface)
done = False
active = False
text = ''
while not done:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            done = True
            break
        if Next_Button.handle_event(ev, main_surface):
            for Box in box_list:
                active = Box.get_selection()
                if active:
                    text = Box.get_text()
                    done = True
                    Next_Button.draw(main_surface)
                    break
        if not done:
            for Box in box_list:
                Box.handle_event(ev)
    for Box in box_list:
        Box.draw(main_surface)
    pygame.display.flip()
print(text)
pygame.quit()

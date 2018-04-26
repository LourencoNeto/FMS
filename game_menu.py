from SimulatorModules import *
from SimulationGame import *
from stop_mune import *
from time import sleep
from copy import copy

def game_menu(home, away, team_home, team_away):
    pygame.event.set_allowed(None)
    pygame.event.set_allowed([pygame.MOUSEBUTTONDOWN, pygame.QUIT])
    surface_height = 230
    surface_width = 580
    main_surface = pygame.display.set_mode((surface_width, surface_height))
    font1 = pygame.font.SysFont(None, 20)
    file_home = "Icones\\" + home + ".png"
    icon_home = pygame.image.load(file_home)
    file_away = "Icones\\" + away + ".png"
    icon_away = pygame.image.load(file_away)
    score_home = 0
    score_away = 0
    home_box = SelectBox(70, 50, 170, home)
    away_box = SelectBox(360, 50, 170, away)
    main_surface.fill((33, 94, 33))
    main_surface.blit(icon_home, (50, 50))
    main_surface.blit(icon_away, (340, 50))
    main_surface.blit(font1.render(str(score_home) + " x " + str(score_away), True, pygame.Color("black")), (280, 52))
    Stop_Button = Button(240, 170, 100, 40, 30, 13, "Pausa")
    Stop_Button.draw(main_surface)
    home_box.draw(main_surface)
    away_box.draw(main_surface)
    home_starting_team = team_home.get_team()
    away_starting_team = team_away.get_team()
    Data_Home_Playing_Team = copy(home_starting_team)
    Data_Away_Playing_Team = copy(away_starting_team)
    Kick_off = kc.Game()
    # Kick_off.field, Home_PlayingTeam, Away_PlayingTeam = Filling_Field(Kick_off, Home_Starting_Team, Away_Starting_Team)
    Kick_off.field, Home_PlayingTeam, Away_PlayingTeam = Filling_Field(Kick_off, home_starting_team, away_starting_team, team_home.get_formation())
    done = False
    quit = False
    altered_formation = False
    while not done and Kick_off.timer <= 89:
        time = Kick_off.timer + 1
        if not done:
            Kick_off.rolling_game(Home_PlayingTeam, Away_PlayingTeam)
            if altered_formation:
                Kick_off.field, Home_PlayingTeam, Away_PlayingTeam = Filling_Field(Kick_off, Data_Home_Playing_Team,
                                                                                   Data_Away_Playing_Team, new_formation)
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                done = True
                quit = True
                break
            if Stop_Button.handle_event(ev):
                altered_formation, team_home_list, new_formation, done = stop_menu(team_home, home)
                if done:
                    quit = True
                    break
                j = 0
                while j < 11:
                    if team_home_list[j]["ID"] != Home_PlayingTeam[j].data["ID"]:
                        Home_PlayingTeam[j] = kc.Player(
                            team_home_list[j], Home_PlayingTeam[j].position, Home_PlayingTeam[j].group_player, "Home",
                            Home_PlayingTeam[j].team_queue)
                        Kick_off.field[Home_PlayingTeam[j].position[0]][Home_PlayingTeam[j].position[1]] = Home_PlayingTeam[j]
                    j += 1
                main_surface = pygame.display.set_mode((surface_width, surface_height))
                main_surface.fill((33, 94, 33))
                main_surface.blit(icon_home, (50, 50))
                main_surface.blit(icon_away, (340, 50))
                main_surface.blit(font1.render(str(score_home) + " x " + str(score_away), True, pygame.Color("black")), (280, 52))
                Stop_Button.draw(main_surface)
                home_box.draw(main_surface)
                away_box.draw(main_surface)
        score_home = Kick_off.scores[0]
        score_away = Kick_off.scores[1]
        if not done:
            Rect1 = pygame.Rect(210, 90, 150, 30)
            Rect2 = pygame.Rect(270, 50, 40, 30)
            pygame.draw.rect(main_surface, pygame.Color(33, 94, 33), Rect2)
            pygame.draw.rect(main_surface, pygame.Color(33, 94, 33), Rect1)
            main_surface.blit(font1.render(str(score_home) + " x " + str(score_away), True, pygame.Color("black")), (280, 52))
            main_surface.blit(font1.render("Tempo de Jogo: " + str(time), True, pygame.Color("black")), (220, 92))
            i = 0
            while i < 11:
                Data_Home_Playing_Team[i] = Home_PlayingTeam[i].data
                Data_Away_Playing_Team[i] = Away_PlayingTeam[i].data
                i += 1
        pygame.display.flip()
        if done:
            break
        sleep(2)
    return quit

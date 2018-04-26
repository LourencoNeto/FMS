import pandas as pd
import pygame
import random


class InputBox:

    def __init__(self, x, y, width, text=''):
        self.height = 20
        self.rect = pygame.Rect(x, y, width, self.height)
        self.color_inactive = pygame.Color("gray")
        self.color_active = pygame.Color("blue")
        self.color_text = pygame.Color("black")
        self.color_rect = self.color_inactive
        self.color_background = pygame.Color("white")
        self.text = text
        self.font = pygame.font.Font(None, 20)
        self.text_surface = self.font.render(self.text, True, self.color_text)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
                print("1")      ###################################################################################################################
            else:
                self.active = False
            self.color_rect = self.color_active if self.active else self.color_inactive
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode ##eliminar os casos em que nao sao simbolos, letras ou numeros e colocar um limite no tamanho da palavra
            self.text_surface = self.font.render(self.text, True, self.color_text)

    def draw(self, main_surface):
        main_surface.fill(self.color_background, self.rect)
        main_surface.blit(self.text_surface, (self.rect.x+5,self.rect.y+2))
        pygame.draw.rect(main_surface, self.color_rect, self.rect, 1)

    def get_text(self):
        return self.text


class Button:

    def __init__(self, x, y, width, height, dx, dy, text=''):
        self.rect = pygame.Rect(x, y, width, height)
        self.color_inactive = pygame.Color("gray")
        self.color_active = pygame.Color("blue")
        self.color_inactive = pygame.Color("gray")
        self.color_active = pygame.Color("blue")
        self.color_text = pygame.Color("black")
        self.color_rect = self.color_inactive
        self.color_background = pygame.Color("white")
        self.text = text
        self.font = pygame.font.Font(None, 20)
        self.text_surface = self.font.render(self.text, True, self.color_text)
        self.dx = dx
        self.dy = dy
        self.active = False

    def draw(self, main_surface):
        main_surface.fill(self.color_background, self.rect)
        main_surface.blit(self.text_surface, (self.rect.x + self.dx, self.rect.y + self.dy))
        pygame.draw.rect(main_surface, self.color_rect, self.rect, 1)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                print("2")  #############################################################################################
                self.active = not self.active
            else:
                self.active = False
            self.color_rect = self.color_active if self.active else self.color_inactive
            return self.active


class SelectBox:
    def __init__(self, x = 0, y = 0, width = 0, text='', active = False):
        self.height = 20
        self.rect = pygame.Rect(x, y, width, self.height)
        self.color_inactive = pygame.Color("gray")
        self.color_active = pygame.Color("blue")
        self.color_text = pygame.Color("black")
        self.color_rect = self.color_inactive
        self.color_background = pygame.Color("white")
        self.text = text
        self.font = pygame.font.Font(None, 20)
        self.text_surface = self.font.render(self.text, True, self.color_text)
        self.active = active


    def draw(self, main_surface):
        main_surface.fill(self.color_background, self.rect)
        main_surface.blit(self.text_surface, (self.rect.x + 5, self.rect.y + 2))
        pygame.draw.rect(main_surface, self.color_rect, self.rect, 1)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
                print("1")      ###################################################################################################################
            else:
                self.active = False
            self.color_rect = self.color_active if self.active else self.color_inactive

    def move_rect(self, dy):
        self.rect = self.rect.move(0, dy)

    def get_text(self):
        return self.text

    def get_selection(self):
        return self.active

    def update_box(self, text):
        self.text = text


class SelectBoxTable:

    def __init__(self, surface, list, x, y, width, dy):
        self.x = x
        self.y = y
        self.width = width
        self.dy = dy
        self.list = []
        self.surface = surface
        self.active_box = SelectBox
        self.active = False
        self.create_table(list, x, y, width, dy)

    def update_table(self, list):
        self.create_table(list, self.x, self.y, self.width, self.dy)

    def create_table(self, list, x, y, width, dy):
        for name in list:
            self.list.append(SelectBox(x, y, width, name))
            y += dy

    def activity(self):
        self.active_box = SelectBox
        self.active = False
        for Box in self.list:
            active = Box.get_selection()
            if active:
                self.active = True
                self.active_box = Box
        return self.active

    def selected_box(self):
        return self.active_box

    def handle_event(self, event):
        for Box in self.list:
            Box.handle_event(event)

    def draw(self):
        for Box in self.list:
            Box.draw(self.surface)

    def print_list(self):
        for Box in self.list:
            print(Box.get_text())


class ManagerTeam:
    def __init__(self, data_team):
        self.data_team = data_team
        self.formation = 442
        self.team = []
        self.reserves = []
        self.substitutes = []
        self.build_team_default()

    def set_formation(self, formation):
        self.formation = formation

    def get_formation(self):
        return self.formation

    def get_list_formation(self):
        if self.formation == 442:
            return ['GK', 'CB', 'CB', 'LB', 'RB', 'CM', 'CM', 'LM', 'RM', 'LS', 'RS']
        if self.formation == 433:
            return ['GK', 'CB', 'CB', 'LB', 'RB', 'CM', 'CM', 'CM', 'LW', 'RW', 'ST']
        if self.formation == 532:
            return ['GK', 'CB', 'CB', 'CB', 'LB', 'RB', 'CM', 'CM', 'CM', 'LS', 'RS']
        if self.formation == 352:
            return ['GK', 'CB', 'CB', 'CB', 'CM', 'CM', 'CM', 'LM', 'RM', 'LS', 'RS']

    def get_possible_formation(self):
        return ['     4 - 4 - 2', '     4 - 3 - 3', '     5 - 3 - 2', '     3 - 5 - 2']

    def build_team_default(self):
        all_gk = self.grouping_by_position("gk")
        all_center_back = self.grouping_by_position("Center Back")
        all_left_back = self.grouping_by_position("Left Back")
        all_right_back = self.grouping_by_position("Right Back")
        all_mid = self.grouping_by_position("Mid")
        all_left_mid = self.grouping_by_position("Left Mid")
        all_right_mid = self.grouping_by_position("Right Mid")
        all_left_forward = self.grouping_by_position("Left Forward")
        all_right_forward = self.grouping_by_position("Right Forward")

        #Construindo time titular default 442
        gk = []
        defenders = []
        mid = []
        forwards = []
        selected = []
        label = 'ID'

        for player1 in all_left_forward:
            forwards.append(player1)
            selected.append(player1)
            break
        for player1 in all_right_forward:
            aux = False
            for player2 in selected:
                if player1[label] == player2[label]:
                    aux = True
            if not aux:
                forwards.append(player1)
                selected.append(player1)
                break
        if len(forwards) != 2:
            print("ERRO, faltam jogadores no ataque")

        for player1 in all_mid:
            aux = False
            for player2 in selected:
                if player1[label] == player2[label]:
                    aux = True
            if not aux:
                mid.append(player1)
                selected.append(player1)
            if len(mid) == 2:
                break
        if len(mid) != 2:
            print("ERRO, faltam jogadores no meio de campo")

        for player1 in all_left_mid:
            aux = False
            for player2 in selected:
                if player1[label] == player2[label]:
                    aux = True
            if not aux:
                mid.append(player1)
                selected.append(player1)
                break
        if len(mid) != 3:
            for player1 in all_mid:
                aux = False
                for player2 in selected:
                    if player1[label] == player2[label]:
                        aux = True
                if not aux:
                    mid.append(player1)
                    selected.append(player1)
                    break
        if len(mid) != 3:
            print("ERRO, faltam jogadores no meio de campo")

        for player1 in all_right_mid:
            aux = False
            for player2 in selected:
                if player1[label] == player2[label]:
                    aux = True
            if not aux:
                mid.append(player1)
                selected.append(player1)
                break
        if len(mid) != 4:
            for player1 in all_mid:
                aux = False
                for player2 in selected:
                    if player1[label] == player2[label]:
                        aux = True
                if not aux:
                    mid.append(player1)
                    selected.append(player1)
                    break
        if len(mid) != 4:
            print("ERRO, faltam jogadores no meio de campo")

        for player1 in all_center_back:
            aux = False
            for player2 in selected:
                if player1[label] == player2[label]:
                    aux = True
            if not aux:
                defenders.append(player1)
                selected.append(player1)
            if len(defenders) == 2:
                break
        if len(defenders) != 2:
            print("ERRO, faltam jogadores na defesa")

        for player1 in all_left_back:
            aux = False
            for player2 in selected:
                if player1[label] == player2[label]:
                    aux = True
            if not aux:
                defenders.append(player1)
                selected.append(player1)
                break
        if len(defenders) != 3:
            for player1 in all_center_back:
                aux = False
                for player2 in selected:
                    if player1[label] == player2[label]:
                        aux = True
                if not aux:
                    defenders.append(player1)
                    selected.append(player1)
                    break
        if len(defenders) != 3:
            print("ERRO, faltam jogadores na defesa")

        for player1 in all_right_back:
            aux = False
            for player2 in selected:
                if player1[label] == player2[label]:
                    aux = True
            if not aux:
                defenders.append(player1)
                selected.append(player1)
                break
        if len(defenders) != 4:
            for player1 in all_center_back:
                aux = False
                for player2 in selected:
                    if player1[label] == player2[label]:
                        aux = True
                if not aux:
                    defenders.append(player1)
                    selected.append(player1)
                    break
        if len(defenders) != 4:
            print("ERRO, faltam jogadores na defesa")

        gk.append(all_gk[0])
        selected.append(all_gk[0])
        if len(selected) < 11:
            print("ERRO, Falta jogador para formacao 442")
        self.team.extend(gk)
        self.team.extend(defenders)
        self.team.extend(mid)
        self.team.extend(forwards)

        #Consturindo o banco de substitutos default de 7 jogadores de acordo com regras da premier league 1 gk, 2 def, 2 mid , 2 for
        gk = []
        defenders = []
        mid = []
        forwards = []
        selected = []

        number = 1
        for player1 in all_left_forward:
            aux = False
            for player2 in selected:
                if player1[label] == player2[label]:
                    aux = True
            for player2 in self.team:
                if player1[label] == player2[label]:
                    aux = True
            if not aux:
                forwards.append(player1)
                selected.append(player1)
                break
        if len(selected) != 1:
            number = 2
        for player1 in all_right_forward:
            aux = False
            for player2 in selected:
                if player1[label] == player2[label]:
                    aux = True
            for player2 in self.team:
                if player1[label] == player2[label]:
                    aux = True
            if not aux:
                forwards.append(player1)
                selected.append(player1)
            if len(forwards) == number:
                break
        number = 4 - len(selected)

        for player1 in all_mid:
            aux = False
            for player2 in selected:
                if player1[label] == player2[label]:
                    aux = True
            for player2 in self.team:
                if player1[label] == player2[label]:
                    aux = True
            if not aux:
                mid.append(player1)
                selected.append(player1)
            if len(mid) == number:
                break

        if (len(selected)) != 4:
            for player1 in all_left_mid:
                aux = False
                for player2 in selected:
                    if player1[label] == player2[label]:
                        aux = True
                for player2 in self.team:
                    if player1[label] == player2[label]:
                        aux = True
                if not aux:
                    mid.append(player1)
                    selected.append(player1)
                if len(mid) == number:
                    break

        if (len(selected)) != 4:
            for player1 in all_right_mid:
                aux = False
                for player2 in selected:
                    if player1[label] == player2[label]:
                        aux = True
                for player2 in self.team:
                    if player1[label] == player2[label]:
                        aux = True
                if not aux:
                    mid.append(player1)
                    selected.append(player1)
                if len(mid) == number:
                    break
        number = 6 - len(selected)

        for player1 in all_center_back:
            aux = False
            for player2 in selected:
                if player1[label] == player2[label]:
                    aux = True
            for player2 in self.team:
                if player1[label] == player2[label]:
                    aux = True
            if not aux:
                defenders.append(player1)
                selected.append(player1)
            if len(defenders) == number:
                break

        if len(selected) != 6:
            for player1 in all_left_back:
                aux = False
                for player2 in selected:
                    if player1[label] == player2[label]:
                        aux = True
                for player2 in self.team:
                    if player1[label] == player2[label]:
                        aux = True
                if not aux:
                    defenders.append(player1)
                    selected.append(player1)
                if len(defenders) == number:
                    break

        if len(selected) != 6:
            for player1 in all_right_back:
                aux = False
                for player2 in selected:
                    if player1[label] == player2[label]:
                        aux = True
                for player2 in self.team:
                    if player1[label] == player2[label]:
                        aux = True
                if not aux:
                    defenders.append(player1)
                    selected.append(player1)
                if len(defenders) == number:
                    break
        number = 7 - len(selected)

        for player1 in all_gk:
            aux = False
            for player2 in selected:
                if player1[label] == player2[label]:
                    aux = True
            for player2 in self.team:
                if player1[label] == player2[label]:
                    aux = True
            if not aux:
                gk.append(player1)
                selected.append(player1)
            if len(gk) == number:
                break

        if len(selected) != 7:
            print("ERRO, sem jogador suficiente para formas substitutos")

        self.substitutes.extend(gk)
        self.substitutes.extend(defenders)
        self.substitutes.extend(mid)
        self.substitutes.extend(forwards)

        #Construindo lista dos jogadores que ficaram na reserva (nao participaram do jogo
        gk = []
        defenders = []
        mid = []
        forwards = []
        selected = []

        for player1 in all_left_forward:
            aux = False
            for player2 in selected:
                if player1[label] == player2[label]:
                    aux = True
            for player2 in self.team:
                if player1[label] == player2[label]:
                    aux = True
            for player2 in self.substitutes:
                if player1[label] == player2[label]:
                    aux = True
            if not aux:
                forwards.append(player1)
                selected.append(player1)
                break

        for player1 in all_right_forward:
            aux = False
            for player2 in selected:
                if player1[label] == player2[label]:
                    aux = True
            for player2 in self.team:
                if player1[label] == player2[label]:
                    aux = True
            for player2 in self.substitutes:
                if player1[label] == player2[label]:
                    aux = True
            if not aux:
                forwards.append(player1)
                selected.append(player1)
                break

        for player1 in all_mid:
            aux = False
            for player2 in selected:
                if player1[label] == player2[label]:
                    aux = True
            for player2 in self.team:
                if player1[label] == player2[label]:
                    aux = True
            for player2 in self.substitutes:
                if player1[label] == player2[label]:
                    aux = True
            if not aux:
                mid.append(player1)
                selected.append(player1)
                break

        for player1 in all_left_mid:
            aux = False
            for player2 in selected:
                if player1[label] == player2[label]:
                    aux = True
            for player2 in self.team:
                if player1[label] == player2[label]:
                    aux = True
            for player2 in self.substitutes:
                if player1[label] == player2[label]:
                    aux = True
            if not aux:
                mid.append(player1)
                selected.append(player1)
                break

        for player1 in all_right_mid:
            aux = False
            for player2 in selected:
                if player1[label] == player2[label]:
                    aux = True
            for player2 in self.team:
                if player1[label] == player2[label]:
                    aux = True
            for player2 in self.substitutes:
                if player1[label] == player2[label]:
                    aux = True
            if not aux:
                mid.append(player1)
                selected.append(player1)
                break

        for player1 in all_center_back:
            aux = False
            for player2 in selected:
                if player1[label] == player2[label]:
                    aux = True
            for player2 in self.team:
                if player1[label] == player2[label]:
                    aux = True
            for player2 in self.substitutes:
                if player1[label] == player2[label]:
                    aux = True
            if not aux:
                forwards.append(player1)
                defenders.append(player1)
                break

        for player1 in all_left_back:
            aux = False
            for player2 in selected:
                if player1[label] == player2[label]:
                    aux = True
            for player2 in self.team:
                if player1[label] == player2[label]:
                    aux = True
            for player2 in self.substitutes:
                if player1[label] == player2[label]:
                    aux = True
            if not aux:
                defenders.append(player1)
                selected.append(player1)
                break

        for player1 in all_right_back:
            aux = False
            for player2 in selected:
                if player1[label] == player2[label]:
                    aux = True
            for player2 in self.team:
                if player1[label] == player2[label]:
                    aux = True
            for player2 in self.substitutes:
                if player1[label] == player2[label]:
                    aux = True
            if not aux:
                defenders.append(player1)
                selected.append(player1)
                break

        for player1 in all_gk:
            aux = False
            for player2 in selected:
                if player1[label] == player2[label]:
                    aux = True
            for player2 in self.team:
                if player1[label] == player2[label]:
                    aux = True
            for player2 in self.substitutes:
                if player1[label] == player2[label]:
                    aux = True
            if not aux:
                gk.append(player1)
                selected.append(player1)
                break

        self.reserves.extend(gk)
        self.reserves.extend(defenders)
        self.reserves.extend(mid)
        self.reserves.extend(forwards)

    def grouping_by_position(self, group):
        group_players = []

        if group == "Right Forward":
            positions = ["st", "rw", "rf", "rs"]
        elif group == "Left Forward":
            positions = ["st", "rw", "rf", "rs"]
        elif group == "Right Mid":
            positions = ["rm", "rdm", "ram", "rwb", "rcm"]
        elif group == "Left Mid":
            positions = ["lm", "ldm", "lam", "lwb", "lcm"]
        elif group == 'Mid':
            positions = ["cm", "cam", "cdm"]
        elif group == "Right Back":
            positions = ["rb", "rcb"]
        elif group == "Left Back":
            positions = ["lb", "lcb"]
        elif group == "Center Back":
            positions = ["cb"]
        else:
            positions = ["gk"]
        for i in range(len(positions)):
            positions[i] = "prefers_" + positions[i]

        for label in positions:
            for index, player in self.data_team.iterrows():
                if player[label]:
                    group_players.append(player)
        return group_players

    def switches(self, group1, player1, group2, player2):
        if group1 == "team" and group2 == "substitutes":
            self.switch_players(1, player1, player2)
        if group1 == "substitutes" and group2 == "team":
            self.switch_players(1, player2, player1)
        if group1 == "team" and group2 == "reserves":
            self.switch_players(2, player1, player2)
        if group1 == "reserves" and group2 == "team":
            self.switch_players(2, player2, player1)
        if group1 == "substitutes" and group2 == "reserves":
            self.switch_players(3, player1, player2)
        if group1 == "reserves" and group2 == "substitutes":
            self.switch_players(3, player2, player1)
        if group1 == "team" and group2 == "team":
            self.switch_players(4, player1, player2)
        if group1 == "substitutes" and group2 == "substitutes":
            self.switch_players(5, player1, player2)
        if group1 == "reserves" and group2 == "reserves":
            self.switch_players(6, player1, player2)

    def switch_players(self, type, player1, player2):
        number = 0
        count = 0
        #Tipo 1, troca entre jogadores do time titular e do banco de substitutos
        if type == 1:
            for player in self.team:
                if player["name"] == player1:
                    number = count
                    break
                count += 1
            aux = self.team[number]
            count = 0
            for player in self.substitutes:
                if player["name"] == player2:
                    self.team[number] = player
                    self.substitutes[count] = aux
                    break
                count += 1

        #Tipo 2, troca entre jogadores do time titular e reserva
        if type == 2:
            for player in self.team:
                if player["name"] == player1:
                    number = count
                    break
                count += 1
            aux = self.team[number]
            count = 0
            for player in self.reserves:
                if player["name"] == player2:
                    self.team[number] = player
                    self.reserves[count] = aux
                    break
                count += 1

        #Tipo 3, troca entre jogadores do banco de substitutos e do time reserva
        if type == 3:
            for player in self.substitutes:
                if player["name"] == player1:
                    number = count
                    break
                count += 1
            aux = self.substitutes[number]
            count = 0
            for player in self.reserves:
                if player["name"] == player2:
                    self.substitutes[number] = player
                    self.reserves[count] = aux
                    break
                count += 1

        # Tipo 4, troca entre jogadores do time titular
        if type == 4:
            for player in self.team:
                if player["name"] == player1:
                    number = count
                    break
                count += 1
            aux = self.team[number]
            count = 0
            for player in self.team:
                if player["name"] == player2:
                    self.team[number] = player
                    self.team[count] = aux
                    break
                count += 1

        # Tipo 5, troca entre jogadores do banco de substitutos
        if type == 5:
            for player in self.substitutes:
                if player["name"] == player1:
                    number = count
                    break
                count += 1
            aux = self.substitutes[number]
            count = 0
            for player in self.substitutes:
                if player["name"] == player2:
                    self.substitutes[number] = player
                    self.substitutes[count] = aux
                    break
                count += 1

        # Tipo 6, troca entre jogadores do time reserva
        if type == 6:
            for player in self.reserves:
                if player["name"] == player1:
                    number = count
                    break
                count += 1
            aux = self.reserves[number]
            count = 0
            for player in self.reserves:
                if player["name"] == player2:
                    self.reserves[number] = player
                    self.reserves[count] = aux
                    break
                count += 1

    def get_team(self):
        return self.team

    def get_substitutes(self):
        return self.substitutes

    def get_reserves(self):
        return self.reserves

    def get_list_team(self):
        list = []
        for player in self.team:
            list.append(player["name"])
        return list

    def get_list_substitutes(self):
        list = []
        for player in self.substitutes:
            list.append(player["name"])
        return list

    def get_list_reserves(self):
        list = []
        for player in self.reserves:
            list.append(player["name"])
        return list


class OpponentsOrder:
    def __init__(self, team):
        database = pd.read_csv('Simulation/Database/FIFA18_database.csv')
        premier_league = database.loc[database.league == 'English Premier League']
        english_teams = premier_league.club.unique().tolist()
        size = len(english_teams)
        index_list = list(range(size))
        random.Random().shuffle(index_list)
        self.away_team_name = []
        self.AwayTeamList = []
        for index in index_list:
            if english_teams[index] != team:
                data_team = database.loc[database.club == english_teams[index]]
                self.AwayTeamList.append(ManagerTeam(data_team))
                self.away_team_name.append(english_teams[index])

    def get_opponent(self, number):
        return self.AwayTeamList[number]

    def get_opponent_name(self, number):
        return self.away_team_name[number]
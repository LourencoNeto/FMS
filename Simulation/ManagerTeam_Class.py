# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 10:10:16 2018

@author: Lourenço Neto
"""

class ManagerTeam:
    def __init__(self, data_team):
        self.data_team = data_team
        self.formation = 442
        self.team = []
        self.reserves = []
        self.substitutes = []
        self.build_team_default()
        

    def set_formation(self,formation):
        self.formation = formation

    def get_formation(self):
        if self.formation == 442:
            return ['gk', 'cb'] ###continuar, procurar outras formacoes

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

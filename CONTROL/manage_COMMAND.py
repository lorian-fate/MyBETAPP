from FOOTBALL.football import Football
from os import system
from CONTROL.manage_DATAS import Manage
import json



class Manage_COMMAND:

    detail_command = {
        'makebet': {
            'league_name': "type a league's name", 
            'name_first_team': "type the first team's name",
            'name_second_team': "type the second team's name",
            'profit_local': "type the profit correspondent to the local team",
            'profit_draw': "type the profit correspondent to a draw",
            'profit_visitor': "type the profit correspondent to the visitor team",
            'amount_to_bet':"type the amount to bet. Is an optional option",
            'e.g':"makebet league_name local_team visitor_team profit_local profit_draw profit_visitro amount_to_bet"
            },
        'show': {
            "recommended bets": "show all recommended bets saved",
            "dangerous bets": "show the last five bet tried",
            "all bets": "show bets's history",
            "success bets": "show all success bets",
            "failed bets": "show all failed bets",
            "total": "show the quantity of all bets and more parameter",
            "e.g": "show total recommended/dangerous/all/... bets"
            },
        'hit':{
            'porcentage': "show the porcentage of an specific file",
            'recommended': "show the porcentage of rcommended bets",
            'dangerous': "show the porcentage of dangerous bets",
            'e.g': "hit porcentage recommended/dangerous"
            },
        'resultbet':{
            "save": "save the result of the bets",
            "recommended": "save the result of all recommended bets",
            "dangerous": "save the result of all dangerous bets",
            "e.g.": "resultbet save recommended/dangerous"
            }
    }
    command_list = {
        'listcommand': 'show all allowed commands',
        'makebet':'take more argument. allow make a new bet',
        'resultbet': "take more argument. allow dealt whit bets's result",
        'hit': "take more argument. show the porcentage",
        'exit': 'exits the program',
        'show': 'take more argument and show that the argument ask',
        'help': "goes after a command and show how use a command in detail. e.g 'makebet help'",
        'clean': "clean your screen"
        }
    obj_manage = Manage()


    @classmethod
    def head(self):
        print("=================================================================")
        print("================== WELCOME TO YOUR BET APP ======================")
        print("=================================================================")
        print("Type 'listcommand' to show allowed commands or 'help' ")


    @classmethod
    def makebet_command(self, keyword_list):
        if keyword_list[-1] == '':
            keyword_list.pop()

        if (len(keyword_list) == 8 or len(keyword_list) == 7) and (keyword_list[0] in self.detail_command.keys()):
            if len(keyword_list) == 8:
                obj_football = Football(keyword_list[1], (keyword_list[2], keyword_list[3]), 
                keyword_list[4], keyword_list[5], keyword_list[6], keyword_list[7])
                if (type(float(keyword_list[4])) == float) and (type(float(keyword_list[5])) == float) \
                    and (type(float(keyword_list[6])) == float):
                    print(obj_football.my_BET())

            elif len(keyword_list) == 7:
                obj_football = Football(keyword_list[1], (keyword_list[2], keyword_list[3]), 
                keyword_list[4], keyword_list[5], keyword_list[6])
                if (type(float(keyword_list[4])) == float) and (type(float(keyword_list[5])) == float) \
                    and (type(float(keyword_list[6])) == float):
                    print(obj_football.my_BET())
        else:
            print("missing arguments")
    

    @classmethod
    def help_command(self, keyword_list):
        if len(keyword_list) == 2:
            if keyword_list[0] in self.detail_command.keys():
                print(F"so you can use '{keyword_list[0]}'")
                for my_command, utility in self.detail_command[keyword_list[0]].items():
                    if 6 <= len(my_command) <= 14:
                        print(my_command.upper(), "\t\t", utility)
                    elif len(my_command) <= 6:
                        print(my_command.upper(), "\t\t\t", utility)
                    else:
                        print(my_command.upper(), "\t", utility)
            else:
                print(f"'{keyword_list[0]}' isn't a inner command of this program")
        else:
            print("command error")


    @classmethod
    def showed_items(self, my_json):
        print("DATE", "\t\t", "LOCAL TEAM", "\t\t", "VISITOR TEAM", "\t\t", 
        "LOCAL WINER", "\t\t", "VISITOR WINER", "\t\t", "DRAW")
        print("============================================================\
=========================================================")
        for my_data in my_json["data"]:
            if len(my_data["local_team"]) < 6 and len(my_data["visitor_team"]) < 6:
                print(my_data["date"], "\t", my_data["local_team"], "\t\t\t", 
                my_data["visitor_team"], "\t\t\t", my_data["local_winer"], 
                "\t\t\t", my_data["visitor_winer"], "\t\t\t", my_data["draw"])

            elif len(my_data["local_team"]) < 6 and len(my_data["visitor_team"]) >= 14:
                print(my_data["date"], "\t", my_data["local_team"], "\t\t\t", 
                my_data["visitor_team"], "\t", my_data["local_winer"], "\t\t\t", 
                my_data["visitor_winer"], "\t\t\t", my_data["draw"])

            elif len(my_data["local_team"]) >= 14 and len(my_data["visitor_team"]) < 6:
                print(my_data["date"], "\t", my_data["local_team"], "\t", 
                my_data["visitor_team"], "\t\t\t", my_data["local_winer"], "\t\t\t", 
                my_data["visitor_winer"], "\t\t\t", my_data["draw"])

            elif len(my_data["local_team"]) >= 14 and len(my_data["visitor_team"]) >= 14:
                print(my_data["date"], "\t", my_data["local_team"], "\t", 
                my_data["visitor_team"], "\t", my_data["local_winer"], "\t\t\t", 
                my_data["visitor_winer"], "\t\t\t", my_data["draw"])

            elif len(my_data["local_team"]) < 6:
                print(my_data["date"], "\t", my_data["local_team"], "\t\t\t", 
                my_data["visitor_team"], "\t\t", my_data["local_winer"], "\t\t\t", 
                my_data["visitor_winer"], "\t\t\t", my_data["draw"])

            elif len(my_data["visitor_team"]) < 6:
                print(my_data["date"], "\t", my_data["local_team"], "\t\t", 
                my_data["visitor_team"], "\t\t\t", my_data["local_winer"], "\t\t\t", 
                my_data["visitor_winer"], "\t\t\t", my_data["draw"])

            elif len(my_data["local_team"]) >= 14:
                print(my_data["date"], "\t", my_data["local_team"], "\t", 
                my_data["visitor_team"], "\t\t", my_data["local_winer"], "\t\t\t", 
                my_data["visitor_winer"], "\t\t\t", my_data["draw"])

            elif len(my_data["visitor_team"]) >= 14:
                print(my_data["date"], "\t", my_data["local_team"], "\t\t", 
                my_data["visitor_team"], "\t", my_data["local_winer"], "\t\t\t", 
                my_data["visitor_winer"], "\t\t\t", my_data["draw"])

            else:
                print(my_data["date"], "\t", my_data["local_team"], "\t\t", 
                my_data["visitor_team"], "\t\t", my_data["local_winer"], "\t\t\t", 
                my_data["visitor_winer"], "\t\t\t", my_data["draw"])


    @classmethod
    def show_command(self, keyword_list):
        if (keyword_list[1].lower() == 'recommended') and (keyword_list[2].lower() == 'bets'):
            with open("./DATAS/FOOTBALL_DATAS/recommended_BETS.json") as my_File:
                my_json = json.load(my_File)
                if len(my_json["data"]) == 0:
                    print("There're any recommended bet yet")
                else:
                    Manage_COMMAND.showed_items(my_json)
                
        elif (keyword_list[1].lower() == 'all') and (keyword_list[2].lower() == 'bets'):
            with open("./DATAS/FOOTBALL_DATAS/historical_BETS.json") as my_File:
                my_json = json.load(my_File)
                if len(my_json["data"]) == 0:
                    print("There're any bet yet")
                else:
                    Manage_COMMAND.showed_items(my_json)

        elif (keyword_list[1].lower() == 'dangerous')  and (keyword_list[2].lower() == 'bets'):
            with open("./DATAS/FOOTBALL_DATAS/dangerous_BETS.json") as my_File:
                my_json = json.load(my_File)
                if len(my_json["data"]) == 0:
                    print("There're any dangerous bet yet")
                else:
                    Manage_COMMAND.showed_items(my_json)

        elif (keyword_list[1].lower() == 'success')  and (keyword_list[2].lower() == 'bets'):
            with open("./DATAS/FOOTBALL_DATAS/success_recommended_BETS.json") as my_File:
                my_json = json.load(my_File)
                if len(my_json["data"]) == 0:
                    print("There're any success bet yet")
                else:
                    Manage_COMMAND.showed_items(my_json)
        
        elif (keyword_list[1].lower() == 'failed')  and (keyword_list[2].lower() == 'bets'):
            with open("./DATAS/FOOTBALL_DATAS/failed_recommended_BETS.json") as my_File:
                my_json = json.load(my_File)
                if len(my_json["data"]) == 0:
                    print("There're any failed bet yet")
                else:
                    Manage_COMMAND.showed_items(my_json)
        
        #elif (keyword_list[1].lower() == 'total'):
            


    @classmethod
    def solo_command(self, command_line):
        if command_line.lower() == 'clean':
            system("cls")
            Manage_COMMAND.head()
        elif command_line.lower() == 'listcommand' or command_line.lower() == 'help':
            for command, utility in self.command_list.items():
                if len(command) <= 6:
                    print(command.upper(),"\t\t",utility)
                else:
                    print(command.upper(),"\t",utility)
        elif command_line.lower() in self.detail_command.keys():
            print(f"The command '{command_line}' need more parameters. Type it with 'help' to more information")
        else:
            print(f"'{command_line}' isn't a inner command of this program")


    @classmethod   
    def hit_command(self, keyword_list):
        
        if (len(keyword_list) == 3) and (keyword_list[1].lower() == 'porcentage') and (keyword_list[2].lower() == 'recommended'):
            file_list = ["success_recommended_BETS", "recommended_BETS"]
            porcentage = self.obj_manage.hit_porcentage(file_list[0], file_list[1])
            print(f"{porcentage[2]} bets of {porcentage[1]} recommended bets was successfully\
            \nThe hit porcetange is: {round(porcentage[0], 2)}%")

        elif (keyword_list[1].lower() == 'porcentage') and (keyword_list[2].lower() == 'dangerous'):
            file_list = ["success_dangerous_BETS", "dangerous_BETS"]
            porcentage = self.obj_manage.hit_porcentage(file_list[0], file_list[1])
            print(f"{porcentage[2]} bets of {porcentage[1]} recommended bets was successfully\
            \nThe hit porcetange is: {porcentage[0]}%")
            
        else:
            if len(keyword_list) == 2 and keyword_list[1] == 'porcentage':
                print("A param is required")
            else:
                for keyword in keyword_list[1:]:
                    if keyword not in self.detail_command["hit"].keys():
                        print(f"'{keyword}' isn't a inner command of this program") 


    @classmethod
    def resultbets_command(self, keyword_list):
        if (keyword_list[1].lower() == 'save') and (keyword_list[2].lower() == 'recommended'):
            file_list = ["success_recommended_Bets", "failed_recommended_Bets", 
                         "recommended_Bets", "current_recommended_BETS"]
            self.obj_manage.result(file_list[0], file_list[1], file_list[2], file_list[3])
        elif (keyword_list[1].lower() == 'save') and (keyword_list[2].lower() == 'dangerous'):
            file_list = ["success_dangerous_Bets", "failed_dangerous_Bets", 
                         "dangerous_Bets", "current_dangerous_BETS"]
            self.obj_manage.result(file_list[0], file_list[1], file_list[2], file_list[3])
        else:
            if len(keyword_list) == 2 and keyword_list[1] == 'save':
                print("A param is required")
            else:
                for keyword in keyword_list[1:]:
                    if keyword not in self.detail_command["resultbet"]:
                        print(f"'{keyword}' isn't a inner command of this program") 
from CONTROL.manage_DATAS import Manage
from CONTROL.calculus import Calculations



class Football:
    obj_manage = Manage()
    obj_calculations = Calculations()

    def __init__(self, league=None, team_tuple=None, local_winer=None, 
    draw=None, visitor_winer=None, amount_to_bet=10):
        self.league = league
        self.team_tuple = team_tuple
        self.local_winer = local_winer
        self.draw = draw
        self.visitor_winer = visitor_winer
        self.amount_to_bet = amount_to_bet
    

    def my_BET(self):
        value_list = [float(self.local_winer), float(self.draw), float(self.visitor_winer)]
        threshold_value = ((max(value_list)*100)/sum(value_list))/100
        main_directory = "./DATAS/FOOTBALL_DATAS/historical_BETS.json"
        self.obj_manage.save_DATA(
                main_directory, self.league, 
                self.team_tuple, self.local_winer, 
                self.draw, self.visitor_winer
            )

        if threshold_value > 0.55:
            value_list.remove(max(value_list))
            mess = "Recommended bet"
            directory = "./DATAS/FOOTBALL_DATAS/current_recommended_BETS.json"
            self.obj_manage.save_DATA(
                directory, self.league, 
                self.team_tuple, self.local_winer, 
                self.draw, self.visitor_winer
            )
            return self.obj_calculations.betFOO_calculations(value_list[0], 
                                                            value_list[1], mess)
            
        elif 0.45 < threshold_value < 0.55:
            value_list.remove(max(value_list))
            obj_calculations = Calculations()
            mess = "Dangerous bet"
            directory = "./DATAS/FOOTBALL_DATAS/current_dangerous_BETS.json"
            self.obj_manage.save_DATA(
                directory, self.league, 
                self.team_tuple, self.local_winer, 
                self.draw, self.visitor_winer
            )
            return self.obj_calculations.betFOO_calculations(value_list[0], 
                                                            value_list[1], mess)
        else:
            return "Not recommended bet"

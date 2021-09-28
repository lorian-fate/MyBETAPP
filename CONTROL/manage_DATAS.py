import json
from datetime import datetime



class Manage:
    
    def save_DATA(
            self, directory,
            league, team_tuple,
            local_winer, draw,
            visitor_winer
                ):
        my_file = open(directory)
        my_data = json.load(my_file)
        my_file.close()
        my_dictionary = {
                    'league': league,
                    'date': datetime.today().strftime("%d-%m-%Y"),
                    'local_team': team_tuple[0],
                    'visitor_team': team_tuple[1],
                    'local_winer': local_winer,
                    'visitor_winer': visitor_winer,
                    'draw': draw
        }
        if my_dictionary not in my_data["data"]:
            my_data["data"].append(my_dictionary)
            with open(directory, "w") as json_File:
                json.dump(my_data, json_File, indent=4)
    

    
    def hit_porcentage(self, success, filename):
        directory1 = f"./DATAS/FOOTBALL_DATAS/{success}.json"
        directory2 = f"./DATAS/FOOTBALL_DATAS/{filename}.json"

        recomended_Bets_file = open(directory2)
        my_data = json.load(recomended_Bets_file)
        recomended_Bets_file.close()

        success_Bets_file = open(directory1)
        success_data = json.load(success_Bets_file)
        success_Bets_file.close()

        lenght_success, lenght_filename = len(success_data["data"]), len(my_data["data"])
        return (lenght_success*100)/lenght_filename, lenght_filename, lenght_success
    

    @classmethod
    def failure(self, match_R):
        bet_value = {
            '1': {'local': float(match_R["local_winer"])},
            '2': {'visitor': float(match_R["visitor_winer"])},
            '3': {'draw': float(match_R["draw"])}
            }
        result_list = [
            float(match_R["local_winer"]),
            float(match_R["visitor_winer"]),
            float(match_R["draw"])
        ]
        value_list = []
        value_list.insert(0, result_list.pop(result_list.index(min(result_list))))
        value_list.insert(0, result_list.pop(result_list.index(min(result_list))))
        while True:
            result_match = input(f'1._local \n2._visitor \n3._draw\
            \nselect the result between {match_R["local_team"]} & {match_R["visitor_team"]}: ')
            if result_match == '1':
                local_value = bet_value['1']['local']
                if local_value in value_list:
                    return True
                else:
                    return False
            elif result_match == '2':
                visitor_value = bet_value['2']['visitor']
                if visitor_value in value_list:
                    return True
                else:
                    return False
            elif result_match == '3':
                draw_value = bet_value['3']['draw']
                if draw_value in value_list:
                    return True
                else:
                    return False
            else:
                print("not value reconized. Try again")
    

    def result(self, success, failed, filename, current_b):
        directory1A = f"./DATAS/FOOTBALL_DATAS/{success}.json"
        directory1B = f"./DATAS/FOOTBALL_DATAS/{failed}.json"
        directory2A = f"./DATAS/FOOTBALL_DATAS/{current_b}.json"
        directory2B = f"./DATAS/FOOTBALL_DATAS/{filename}.json"

        recomended_Bets_file = open(directory2A)
        my_data = json.load(recomended_Bets_file)
        recomended_Bets_file.close()

        current_Bets = open(directory2B)
        my_current = json.load(current_Bets)
        current_Bets.close()

        success_Bets_file = open(directory1A)
        success_data = json.load(success_Bets_file)
        success_Bets_file.close()

        failed_Bets_file = open(directory1B)
        failed_data = json.load(failed_Bets_file)
        failed_Bets_file.close()

        for match_bet in my_data["data"]:

            if match_bet not in my_current["data"]:
                my_current["data"].append(match_bet)
                with open(directory2B, "w") as my_file:
                    json.dump(my_current, my_file, indent=4)

            if (match_bet not in success_data["data"]) and (match_bet not in failed_data["data"]):
                result_match = Manage.failure(match_bet)
                if result_match == True:
                    success_data["data"].append(match_bet)
                    with open(directory1A, 'w') as json_File:
                        json.dump(success_data, json_File, indent=4)
                else:
                    failed_data["data"].append(match_bet)
                    with open(directory1B, 'w') as json_File:
                        json.dump(failed_data, json_File, indent=4)
        
        my_data["data"].clear()
        with open(directory2A, "w") as my_file:
            json.dump(my_data, my_file, indent=4)
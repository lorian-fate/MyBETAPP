



class Calculations:
    amount_to_bet = 10
    

    @property
    def value_generators(self):
        x = 0
        for i in range(self.amount_to_bet*100):
            x += 0.01
            y = self.amount_to_bet - x
            my_tuple = (round(x, 2), round(y, 2))
            yield my_tuple
    

    def betFOO_calculations(self, first_value, second_value, mess):

        for my_tuple in self.value_generators:
            
            if (my_tuple[0]*first_value > self.amount_to_bet) and \
            (my_tuple[1]*second_value > self.amount_to_bet):
                profit_1 = (my_tuple[0]*first_value) - self.amount_to_bet
                profit_2 = (my_tuple[1]*second_value) - self.amount_to_bet
                my_sust = round((profit_2 - profit_1), 3)
                
                if -0.035 <= my_sust <= 0.035:
                    return f"Bet {my_tuple[0]} to {first_value} and your profit will be {round(profit_1, 2)}\
                           \nBet {my_tuple[1]} to {second_value} and your profit will be {round(profit_2, 2)}\
                           \nNota: {mess}"


    def betBAS_calculations(self, first_value, second_value):
        values_given = [first_value, second_value]
        value_one = max(values_given)
        value_two = min(values_given)
        mattress_value = self.amount_to_bet * 0.85
        profit_value = self.amount_to_bet * 1.1
        
        for my_tuple in self.value_generators:

            if (my_tuple[0]*value_one >= mattress_value) and \
                (my_tuple[1]*value_two >= profit_value):
                return [(my_tuple[0], value_one), (my_tuple[1], value_two)]

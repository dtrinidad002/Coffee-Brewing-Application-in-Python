class BrewCalculations:
    ''' This class calculates brew times and ratios '''
    def __init__(self, brew_method, servings):
        self.brew_method = brew_method
        self.servings = servings
        self.brew_ratio = self.get_ratio()
        self.time_target = self.get_timing()


    def get_timing (self):
        #Target brew time range  (key = serving size)(values: seconds)
        p_over ={1: (150, 180), 2: (300, 330), 3: (438, 436), 4: (600, 630)}
        f_press = {1: (240, 260), 2: (480, 500), 3: (720, 740), 4: (960, 980)}

        #providing the brew time target range for each combination of brew and serving size
        if self.brew_method == "C":  #flair espresso only has one target time
            time_range = 35 - 45
            #
        elif self.brew_method == "A" and self.servings == 1:
            time_range = p_over.get(0)
        elif self.brew_method == "A" and self.servings == 2:
            time_range = p_over.get(1)
        elif self.brew_method == "A" and self.servings == 3:
            time_range = p_over.get(2)
        elif self.brew_method == "A" and self.servings == 4:
            time_range = p_over.get(3)
        elif self.brew_method == "B" and self.servings == 1:
            time_range = f_press.get(1)
        elif self.brew_method == "B" and self.servings == 2:
            time_range = f_press.get(2)
        else:
            time_range = f_press.get(3)
        #return time range to the get timing function
        return time_range

        #function to output the coffee ratio (grams/ml)
    def get_ratio(self):
        #theres only 1 ratio for espresso method
        if self.brew_method != "C":
            #limiting innner conditional to pour over and french press method
            if self.servings == 1:
                cw_ratio =  "Ratio: 15g coffee : 250ml water "
            elif self.servings == 2:
                cw_ratio = "Ratio: 30g coffee : 500ml water"
            elif self.servings == 3:
                cw_ratio = "Ratio: 45g coffee : 750ml water"
            else:
                cw_ratio = "Ratio: 60g coffee : 1000ml water"
        else:
            cw_ratio = "Ratio: 15g coffee : 35ml water"

        #return cw_ratio back to function
        return cw_ratio

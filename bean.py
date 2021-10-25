import datetime

class Bean:
    """Represents attributes of a coffe bean to create an object"""

    def __init__(self):
        self.bean_origin, self.roast, self.temp = self.pick_region()
        self.roast_date, self.days_past_roast, self.freshness = self.check_freshness()
        self.flavor = self.get_flavor()


    #Function returns bean_origin, roast_type, and reccomended brew temperatures

    def pick_region(self):
        print("|SELECT Origin (pick A,B,C,D)|")
        print("+"+"-"*30+"+")
        print("|      A: Columbia           |")
        print("|      B: Guatamala          |")
        print("|      C: Ethiopia           |")
        print("|      D: Costa Rica         |")
        print("+"+"-"*30+"+")

        #exception handling for inputs that are non
        try:
            bean_origin = input("Your Selection:  ").upper()
        except ValueError:
            print('""""Only enter A B C D (just 1)"""')

        print(" ")
        print(" ")

        print("| SELECT Roast (enter A,B,or C)|")
        print("+"+"-"*30+"+")
        print("|      A: Light                |")
        print("|      B: Medium               |")
        print("|      C: Dark                 |")
        print("+"+"-"*30+"+")
        #brew temperature dictionary with key values from Roast selection
        #Value pairs = target brew temperature.
        temp_dict = {"A":208, "B":204, "C": 200}

        #While function used define roast_type with input function
        while True:
            try:
                roast_type = input("Your Selection:  ")
                #Input matched against the temp_dict to get target brew temperature
                roast_type = roast_type.upper()
                brew_temp = temp_dict[roast_type]
                #exception error to handle key value entries that are not "A, B or C"
            except KeyError:
                print("Please only select either 'A', 'B', or 'C'.")
                continue
            else:
                break
        return bean_origin, roast_type, brew_temp

    def check_freshness(self):
        #input the roast date from the bag must be between 1 and 12
        year = int(input("enter year of the roast: "))

        while year !=2021:
            year = int(input("enter month of the roast: "))
            print("Type 4 digits for 2021")

        month = int(input("enter month of the roast: "))

        while month > 12 or month < 1:
            month = int(input("enter month of the roast: "))
            print("enter only numbers 1 - 12")

       #days cant be more than 31 or less than 1.
        day = int(input("enter day of the month: "))
        while day > 31 or day < 1:
            print("enter only numbers 1 - 12")

            day = int(input("enter day of the month: "))

        bag_date = datetime.datetime(int(year),int(month),int(day))
        #use datetime.now function to get the current date
        today = datetime.datetime.now()
        #get the total

        days_past = int((today - bag_date).days)

        #checks that Beans are within target range of 14 - 25 day
        if days_past > 14  and days_past < 25 :   #if the roast date is above 30 days
            freshness =   "Beans are at peak freshness! \nYou should be able to taste the flavor notes"
        if days_past < 14:
            freshness = "beans are a not within its peak freshness \n It's reccomended to wait 2 weeks after the date of the roast"
        else:
            freshness= "Beans are beyond past freshness.\nFlavor notes less prominent"
        #return days_past_roast and freshness back to function
        print(f'Days past: {days_past}')
        print(f'Freshness: {freshness}')
        #return values back to check_freshness function
        return bag_date, days_past, freshness

    def get_flavor(self):
        #flavor proviles of relevant bean origin
        flavor_dict={
                    "A":{"Columbia: mellow, caramel, ripe"},
                    "B":{"Guatamala: floral, summery, aromatic"},
                    "C":{"Ethiopia: fruity, dense, wine"},
                    "D": {"Costa Rica: bright, creamy, balenced"},
                    }
        flavor = flavor_dict[self.bean_origin]
        return flavor

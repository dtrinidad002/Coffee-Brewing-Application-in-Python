import datetime

class Result:
    """Represents the last feedback object in the program
    Attributes:
    measured_brew time = (seconds)
    """

    #initialize
    def __init__(self, brew_method, time_target, bean_flavor):
        self.brew_method = brew_method
        self.time_target = time_target
        self.bean_flavor = bean_flavor
        self.brew_result = self.reviewTime()

    #main function that compares user input time and compares with the target
    def reviewTime(self):
        print("|====================================|")
        print("when brew is complete \n pause stop watch and log results")
        print("|                                    |")

        while True:
            try:
                min = int(input("enter minutes as an integer. (if < 0 enter '0')"))
                sec = int(input('enter seconds as integer'))
                self.actual_time = int((min * 60) + sec)
            except ValueError:
                print ('please only enter integers')
                print(f"You're final brew time in sec: {actual_time}")
            else:
                break

        if self.actual_time in range(self.time_target[0], self.time_target[1]):
            print("!!!--------!!!!")
            print ("Nicely done!!!")
            print("!!----------!!!")
            brew_result = "Pass"
        elif self.actual_time < self.time_target[0]:
            print(f'Oh no! You May have under extracted! shorter brew times have a tendancy to be bland')
            print('--------------------------------------')
            print(f"""You're probably experiencing bitter coffee \n
            here's some info on the flavor to expect had you extracted properly \n
            {self.bean_flavor}""")
            brew_result = "Fail"
        else:
            print('''Uh oh! You May have over extracted! \n Specialty coffee from this Origin are delicate and when
             soak for too long have a tendancy to get over \n extracted here are some flavor notes of the bean''' )
            print('--------------------------------------')
            print(f"""You're probably experiencing bitter coffee n\
            here's some info on the flavor to expect had you extracted properly \n
            {self.bean_flavor}""")
            brew_result = "Fail"

        return brew_result



class BrewMethod:
    """Represents 3 different objects for brewing coffee manually
    Attributes:
    brew_method (string)
    show_method (string)
    servings (int)"""

    #initialize Class Method Attributes
    #attribute variables are directly linked to functions for easy calls to the main
    def __init__(self):
        self.brew_method, self.grind_size = self.get_method()
        self.servings = self.get_servings()

        #present method options to user
        #print statements used to box to display options
    def get_method(self):
        print("| SELECT METHOD(enter A,B,or C)|")
        print("+"+"-"*30+"+")
        print("|      A: Pour-Over            |")
        print("|      B: French Press         |")
        print("|      C: Flair Espresso       |")
        print("+"+"-"*30+"+")

        try:
            select_method = input('Your Selection:  ').upper() #user enters string letter for A B or C
        except ValueError:
            print('""""Only enter A B C D (just 1)""""')

        if select_method == "A":
            grind_size = "med-fine"
        elif select_method == "B":
            grind_size = "course"
        else:
            grind_size = "fine"
        #attributes for method are defined and returned to the function
        
        return select_method, grind_size
    #function to determing brew beans to water ratio (g:ml )
    def get_servings(self):
        if self.brew_method != "C":
            print("+"+"-"*20+"+")
            print("|SELECT SERVING SIZE   |")
            print("|         1            |")
            print("|         2            |")
            print("|         3            |")
            print("|         4            |")
            print("+"+"-"*20+"+")
            serving_size = input ('Your selection: ')
            return serving_size
        else:
            print('Flair defualt serving size is 1')
            return 1

###-----Imports---------###

import datetime
import csv
from barista import Barista
from bean import Bean
from method import BrewMethod
from result import Result
from brew_calc import BrewCalculations



def main():
    """Main: this is the entry point of the script which starts the user log in Class"""

    #

    ##initialize classes
    user = Barista()
    coffee = Bean()
    guide = BrewMethod()
    brewCalc = BrewCalculations(guide.brew_method, guide.servings)
    outcome = Result(guide.brew_method, brewCalc.time_target, coffee.flavor)


if __name__ == "__main__":
    main()

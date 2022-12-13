import json
from tkinter import *
from tkinter import filedialog
import time

RUN = 1
QUIT = 0


def main():

    choice = 10

    while choice != QUIT:
        choice = menu_choice()    

        
        if choice == RUN:
            beauty()
        elif choice == QUIT:
            print("Bye! :)", end=' ')
            time.sleep(1)
            print('.', end=' ')
            time.sleep(1)
            print('.', end=' ')
            time.sleep(1)
            print('.', end=' ')


def menu_choice():
    print()
    print('Please choose a valid menu option')
    print('---------------------------')
    print('0. Quit Program')
    print('1. Open JSON beautifier')
    

    choice = int(input('Enter your choice: '))
    while choice < QUIT or choice > RUN:
        choice = int(input('Enter a valid menu option: '))

    return choice

def beauty():
    # Create Python object from JSON string data
    path = filedialog.askopenfilename(initialdir="%userprofile%\documents", title="Select a file", filetypes=(("json files", "*.json"),("text files","*.txt")))


    with open(path, "r") as file:
        obj = json.load(file)
 
        # Pretty Print JSON
        pretty_j = json.dumps(obj, indent=4)
        print(pretty_j)



main()

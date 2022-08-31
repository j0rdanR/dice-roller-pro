# bring util functions into scope from other file
from functions import *

def main():
    print_heading(1, "Dice Roller Pro!")

    # while loop continues to ask for input until 'x' is entered
    exit = False
    while exit != True:
        option = input("Enter a roll ('h' for help, 'x' to exit): ")
        option = option.strip().lower()

        # check input matches menu option, and pass to function
        if option == 'h':
            show_help_screen()
        elif option == 'x':
            print_heading(3, "Goodbye!")
            exit = True
        elif option != '':
            # call roll dice function and pass user input.
            # returns bool for if input is valid
            is_valid = roll_dice(option)
            if is_valid == False:
                print("Invalid input\n")





if __name__ == "__main__":
    # wraps entire program in try-except to catch any
    # unexpected errors from stopping program
    try:
        main()
    except Exception as err:
        print(f"\nA problem occurred when running the program.\nErr info: [{err}]\n")
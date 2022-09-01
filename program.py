# DICE ROLLER PRO
# BY JORDAN RODRIGUES

# the functions are defined at the top. You will find the main func at the end.
# all code is commented where necessary, or you can find an explaination on the GitHub repo:
# https://github.com/j0rdanR/dice-roller-pro/blob/main/README.md

# import required modules
import random, time


def print_heading(margin_top, title):
    # options for heading  
    mt = "\n"*margin_top
    length = 60
    divider = "="*length
    title = f"|    {title.upper()}    |"

    # format heading template
    template = f"{mt}{divider}\n{title.center(length)}\n{divider}\n"
    print(template)


def show_help_screen():
    # print information for help screen
    print_heading(3, "Help!")
    print("Enter roll in “[quantity]d[sides]” format.\ne.g. Enter 4d6 to roll four six-sided dice.\n\n")


def roll_dice(input_string):
    # split string in format '[quantity]d[sides]' into array
    # then check if it contains two params (quantity and sides)
    params = input_string.split('d')
    if len(params) != 2:
        return False

    # try-except catches a int conversion error and returns
    # invalid input to the user
    try:
        quantity = int( params[0] )
        sides = int( params[1] )
    except:
        return False

    # checks that the roll params are possible (eg. can't roll
    # a one-sided dice)
    if quantity < 1 or sides < 2:
        return False

    print(f"\nRolling {input_string}:\n")

    # while loop iterates through `quantity` variable to roll
    # dice n times
    i = 0
    rolls = []
    while i < quantity:
        # num is a random number between 1 and `sides` to
        # simulate rolling a dice
        num = random.randint(1, sides)
        
        # add roll outcome to `rolls` array for later use
        rolls.append(num)

        # add delay between outputting 'Rolled a ...!' for
        # the effect of rolling dice
        if i < 15:
            time.sleep(1/quantity)

        print(f"Rolled a {num}!")
        i += 1

    # call stats function and pass `rolls` array
    time.sleep(0.5)
    get_statistics(rolls)


def get_statistics(rolls):
    print_heading(1, "Roll Statistics")

    # calculate basic statistics using math lib
    total = sum(rolls)
    average = round( total / len(rolls) , 2)
    minimum = min(rolls)
    maximum = max(rolls)

    # using a dictionary to format a 'table'
    stats = {
        "Rolls": rolls,
        "Total": total,
        "Average": average,
        "Minimum": minimum,
        "Maximum": maximum,
    }

    # call format_table function with stats dictionary
    print(format_table(stats) + "\n\n")


def format_table(data):
    # takes dictionary and formats each key-value pair so that
    # columns align in output
    table_string = ""
    for key, value in data.items():
        header = f"{key}:{' '*(14 - (len(key)+1))}"
        table_string += f"{header}{value}\n"
    
    return table_string











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
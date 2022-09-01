> Please read this document before attempting to run the program. If you are using the `program.min.py` file then you can skip to [Explaining the code](#explaining-the-code)

<br>

# Dice Roller Pro - Code explaination

11 Computer Science: Task 8 - Jordan Rodrigues


<br>

### Table of Contents
- [Explaining the code](#explaining-the-code)
	- [main.py](#mainpy)
	- [functions.py](#functionspy)


<br>


## Explaining the code

The program is separated into two files for readability. Within the source code you will find the `main.py` and `functions.py` files.

The `main.py` file contains the code for initialising the program and starting the menu loop. As the name suggests, it is the main file, and all functions imported from the other file are called within the menu loop.

The `functions.py` file contains the business logic for the program, as well as utility functions (such as print_heading()) to make the code cleaner. These functions are brought into scope when imported from the main file.

> The code contains comments which define the purpose and intent behind functions/logic, however, you can read on for a more in depth explaination.


<br>

### main.py

This file has the following import:

```python
from functions import *
```

This brings the functions from the `functions.py` module into the scope of the main file.


<br><br>


The program starts with the initial code running:

```python
if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        print(f"\nA problem occurred when running the program.\nErr info: [{err}]\n")
```

The purpose of checking that `__name__ == "__main__"` is to ensure that the file is not being run as a module. Within the if statement, a try-except is used to catch any unexpected runtime errors that may hard crash the program.

It calls the main function, which will be covered next.


<br><br>


The `main()` function looks like this:

```python
def main():
    print_heading(1, "Dice Roller Pro!")

    exit = False
    while exit != True:
        option = input("Enter a roll ('h' for help, 'x' to exit): ")
        option = option.strip().lower()

        if option == 'h':
            show_help_screen()
        elif option == 'x':
            print_heading(3, "Goodbye!")
            exit = True
        elif option != '':
            is_valid = roll_dice(option)
            if is_valid == False:
                print("Invalid input\n")
```

You may notice that it first calls the `print_heading()` function. The code for this will be explained later, but for now you should understand that it is responsible for printing the large welcome banner.

After that, the `exit` variable is initialised with the value of `False`. Once the loop begins, it will continue to run until the variable is updated to `True`.

Within the loop, the user's input is captured and immediately stripped and converted to lowercase. This is to accommodate for an input with capital letters.

Then an if statement is used to compare the input with the menu options. If it matches, the respective code is executed. If anything else is entered, it will assume it is a roll, and pass it off to the `roll_dice()` function. If nothing is entered, the while loop runs again.

The `roll_dice()` function has a return type of `Boolean`. If the function determines that the input is not formatted correctly, it will return `False`, and the program will output 'Invalid input' before looping again.

<!-- <details> -->
<summary>View Pseudocode</summary><br>

```
function main()
	call print_heading()
	set exit to false
	dowhile (exit != true)
		input "select an option...
		set option to input
		if (option == 'h') then

		endif
	end
end
```

</details>

<details>
<summary>View trace table</summary><br>

|Line|Statement|exit|option|Output|
|--|--|--|--|--|
|1|`def main():`|
|2|`print_heading(1, "Dice Roller Pro!")`|||====...|
|4|`exit = False`|`False`|
|5|`while exit != True:`|`False`|
|6|`option = input("Enter a ...")`|`False`|`{user_input}`|Enter a...|
|7|`option = option.strip().lower()`|`False`|`{user_input}`|
|9|`if option == 'h':`|`False`|`'h'`|
|9|`show_help_screen()`|`False`|`'h'`|====...|
|10|`elif option == 'x':`|`False`|`'x'`|
|11|`print_heading(3, "Goodbye!")`|`False`|`'x'`|====...|
|12|`exit = True`|`True`|`'x'`|
|13|`elif option != '':`|`False`|`''`|
|14|`is_valid = roll_dice(option)`|`False`|`''`|
|15|`if is_valid == False:`|`False`|`''`|
|16|`print("Invalid input\n")`|`False`|`''`|Invalid input|


</details>


<br><br>


### functions.py

This file has the following imports:

```python
import sys, random, time
```

The use of these modules will be described later.


<br><br>


The `print_heading()` function takes two arguments: the amount of lines to add as a margin, and the title of the heading.

```python
def print_heading(margin_top, title): 
    mt = "\n"*margin_top
    length = 60
    divider = "="*length
    title = f"|    {title.upper()}    |"

    template = f"{mt}{divider}\n{title.center(length)}\n{divider}\n"
    print(template)
```

The code is split over several lines, and uses variables to make the purpose of each segment clear. The function is self explanatory, and does what you would expect.


<br><br>


The `show_help_screen()` function is simple, and just makes things cleaner than having the code in the main loop.

```python
def show_help_screen():
    print_heading(3, "Help!")
    print("Enter roll in “[quantity]d[sides]” format.\ne.g. Enter 4d6 to roll four six-sided dice.\n\n")
```


<br><br>


The `roll_dice()` function takes the unformatted input string (from the main loop) and handles the main logic for 'rolling the dice'.

```python
def roll_dice(input_string):
    params = input_string.split('d')
    if len(params) != 2:
        return False

    try:
        quantity = int( params[0] )
        sides = int( params[1] )
    except:
        return False

    if quantity < 1 or sides < 2:
        return False

    print(f"\nRolling {input_string}:\n")

    i = 0
    rolls = []
    while i < quantity:
        num = random.randint(1, sides)
        rolls.append(num)

        if i < 15:
            time.sleep(1/quantity)

        print(f"Rolled a {num}!")
        i += 1

    time.sleep(0.5)
    get_statistics(rolls)
```

The comments (in the source code file) describe each line in depth, but the basic steps of this function are to validate the input is formatted correctly, and then to generate a random number based on the paramaters from the input. This function uses the `time` and `random` modules.

The function then passes the roll data to a different function to calculate and print the statistics.


<br><br>

This function takes the array of roll values from the `roll_dice()` function and calculates a variety of statistics by performing mathmatical operations on the roll data.

```python
def get_statistics(rolls):
    print_heading(1, 'Roll Statistics')

    total = sum(rolls)
    average = round( total / len(rolls) , 2)
    minimum = min(rolls)
    maximum = max(rolls)

    stats = {
        "Rolls": rolls,
        "Total": total,
        "Average": average,
        "Minimum": minimum,
        "Maximum": maximum,
    }

    print(format_table(stats) + "\n\n")
```

The statistics are then stored as a dictionary to easily pass it to the `format_table()` function (which is purely for aesthetics).

The `format_table()` function returns a string which represents a uniform table layout when outputted.

```python
def format_table(data):
    table_string = ""
    for key, value in data.items():
        header = f"{key}:{' '*(14 - (len(key)+1))}"
        table_string += f"{header}{value}\n"
    
    return table_string

```


<br><br>

[Back to top](#table-of-contents)
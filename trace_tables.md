
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

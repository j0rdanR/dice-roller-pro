## Trace tables


#### Init:

|Line|Statement|`__name__`|Output|
|--|--|--|--|
|1|`if __name__ == "__main__":`|`"__main__"`|
|2|`try:`|`"__main__"`|
|3|`main()`|`"__main__"`|
|4|`except Exception as err:`|`"__main__"`|
|5|`print("A problem occurred...")`|`"__main__"`|A problem occurred...|


<br>

#### Main function:

|Line|Statement|`exit`|`option`|Output|
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


<br>

#### Rolling dice with different inputs

These trace tables test the program when entering a roll input. They only focus on the `roll_dice()` function, as it is responsible for handling the input and rolling the dice.

The function:
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

<br>

1. `roll_dice()` function with test value: `"1d18"`.

|Line|Statement|`input_string`|`params`|Output|
|--|--|--|--|--|
|1|`def roll_dice(input_string):`|`"1d18"`|`None`
|2|`params = input_string.split('d')`|`"1d18"`|`['2', '14']`
|3|`if len(params) != 2:`|`"1d18"`|`['2', '14']`
|Line|Statement|`quantity`|`sides`|Output|
|5|`try:`|`None`|`None`
|6|`quantity = int( params[0] )`|`2`|`None`
|7|`sides = int( params[1] )`|`2`|`14`
|10|`if quantity < 1 or sides < 2:`|`2`|`14`
|12|`print("Rolling {input_string}:")`|`2`|`14`|Rolling 1d18:|
|Line|Statement|`i`|`quantity`|`rolls`|Output|
|13|`i = 0`|`0`|`1`|`None`
|14|`rolls = []`|`0`|`1`|`[]`
|15|`while i < quantity:`|`0`|`1`|`[]`
|16|`num = random.randint(1, sides)`|`0`|`1`|`[]`
|17|`rolls.append(num)`|`0`|`1`|`[14]`
|18|`if i < 15`|`0`|`1`|`[14]`
|20|`print("Rolled a {num}")`|`0`|`1`|`[14]`
|21|`i += 1`|`1`|`1`|`[14]`
|22|`time.sleep(0.5)`|`1`|`1`|`[14]`
|23|`get_statistics(rolls)`|`1`|`1`|`[14]`

This test concluded with one roll of `14`. Missing lines (such as line 4) are the content of a condition which didn't run, and hence aren't a part of the trace.


<br><br>


2. `roll_dice()` function with test value: `"2d6"`.

|Line|Statement|`input_string`|`params`|Output|
|--|--|--|--|--|
|1|`def roll_dice(input_string):`|`"2d6"`|`None`
|2|`params = input_string.split('d')`|`"2d6"`|`['2', '6']`
|3|`if len(params) != 2:`|`"2d6"`|`['2', '6']`
|Line|Statement|`quantity`|`sides`|Output|
|5|`try:`|`None`|`None`
|6|`quantity = int( params[0] )`|`2`|`None`
|7|`sides = int( params[1] )`|`2`|`6`
|10|`if quantity < 1 or sides < 2:`|`2`|`6`
|12|`print("Rolling {input_string}:")`|`2`|`6`|Rolling 2d6:|
|Line|Statement|`i`|`quantity`|`rolls`|Output|
|13|`i = 0`|`0`|`2`|`None`
|14|`rolls = []`|`0`|`2`|`[]`
|15|`while i < quantity:`|`0`|`2`|`[]`
|16|`num = random.randint(1, sides)`|`0`|`2`|`[]`
|17|`rolls.append(num)`|`0`|`2`|`[4]`
|18|`if i < 15`|`0`|`2`|`[4]`
|20|`print("Rolled a {num}")`|`0`|`2`|`[4]`
|21|`i += 1`|`1`|`2`|`[4]`
|15|`while i < quantity:`|`1`|`2`|`[4]`
|16|`num = random.randint(1, sides)`|`1`|`2`|`[4]`
|17|`rolls.append(num)`|`1`|`2`|`[4, 1]`
|18|`if i < 15`|`1`|`2`|`[4, 1]`
|20|`print("Rolled a {num}")`|`1`|`2`|`[4, 1]`
|21|`i += 1`|`2`|`2`|`[4, 1]`
|22|`time.sleep(0.5)`|`2`|`2`|`[4, 1]`
|23|`get_statistics(rolls)`|`2`|`2`|`[4, 1]`

This test concluded with two rolls of `4` and `1`


<br><br>


3. `roll_dice()` function with test value: `"22"`.

|Line|Statement|`input_string`|`params`|Output|
|--|--|--|--|--|
|1|`def roll_dice(input_string):`|`"22"`|`None`
|2|`params = input_string.split('d')`|`"22"`|`["22"]`
|3|`if len(params) != 2:`|`"22"`|`["22"]`
|4|`return False`

This test concluded and the `roll_dice` function returned `False`, causing the program to output `"Invalid input"`. Note that the print statement is in the main loop, outside of the scope of this trace table.


<br><br>

4. `roll_dice()` function with test value: `"$d6"`.

|Line|Statement|`input_string`|`params`|Output|
|--|--|--|--|--|
|1|`def roll_dice(input_string):`|`"$d6"`|`None`
|2|`params = input_string.split('d')`|`"$d6"`|`['$', '6']`
|3|`if len(params) != 2:`|`"$d6"`|`['$', '6']`
|Line|Statement|`quantity`|`sides`|Output|
|5|`try:`|`None`|`None`
|6|`quantity = int( params[0] )`|`2`|`None`
|8|`except:`
|9|`return False`|`None`|`None`

This test concluded and the `roll_dice` function returned `False`, causing the same effect as the previous test. This time the function encountered an error when converting `'$'` to an int, which was caught by the try-except, returning `False` immediately.
<!-- haskell and fortran work well with pseudocode for syntax highlighting -->

```fortran
Main Module
    Begin
    Call print_heading

    exit <- false

    Dowhile (exit != true)
		option <- Input("Enter a roll...")
		
		If (option == 'h') Then
            Call show_help_screen
        Else If (option == 'x') Then
            Call print_heading Pass 3, "Goodbye!"
            exit <- true
        Else If (option == '') Then
            is_valid <- Call roll_dice
            If (is_valid == false) Then
                Output("Invalid output")
            Endif
        Endif
	Enddo

End Module
```

```haskell
print_heading Module
    Begin
    mt <- Param(margin_top)
    Set length to 60
    divider <- "="*length
    title <- "|  {make title uppercase}  |"

    template <- "{mt}{divider}{title.center(length)}{divider}"
    Output(template)

End Module
```

```haskell
show_help_screen Module
    Begin
    Call print_heading Pass 3, "Help!"
    Output("Enter roll in...")

End Module
```

```haskell
roll_dice Module
    Begin
    params <- Param(input_string.split('d'))
    If (length of params != 2) Then
        return false
    Endif

    Try
        quantity <- convert params[0] to int
        sides <- convert params[1] to int
    Catch
        return false
    Endtry

    If (quantity < 1 or sides < 2) Then
        return false
    Endif

    Output("Rolling {Param(input_string)}")

    Set i to 0
    Set rolls to empty array
    Dowhile (i < quantity)
        num <- generate random number
        rolls <- rolls + num
        Output("Rolled a {num}")
        i <- i + 1
    Enddo

    Call get_statistics Pass rolls

End Module
```


```haskell
get_statistics Module
    Begin
    Call print_heading Pass 1, "Roll Statistics"

    total <- total sum of rolls
    average <- average of rolls
    minimum <- min value of rolls
    maximum <- max value of rolls

    Set stats to object containing statistics

    Output( Call format_table Pass stats )

End Module
```


```haskell
format_table Module
    Begin
    Set table_string to ""
    For each key, value in Param(stats) do
        header <- "{key}:       "
        table_string <- table_string + "{header}{value}"
    Enddo

    return table_string

End Module
```
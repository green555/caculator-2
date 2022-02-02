"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code









#creat a while true loop
#ask user input
#tokenize the input
#if statement for addition
#elif statments for the rest of operations
#return the result
#print the result
#if input is invalid ask the user to re input
#if the user input "q" quit the program



#creat a while true loop
#ask user input
#toke the input
#if statement for addition
#elif statments for the rest of operations
#return the result
#print the result
#if input is invalid ask the user to re input
#if the user input "q" quit the program

flag = True
while flag:
    my_str = input('>')
    
    my_str_to = my_str.split(' ')
    
    fun = my_str_to[0]
    if fun == 'q':
        break
    elif fun == '+':
        num1 = float(my_str_to[1])
        num2 = float(my_str_to[2])
        result = add(num1, num2)
        print(result)
        flag = False


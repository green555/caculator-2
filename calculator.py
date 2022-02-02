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
    to_len = len(my_str_to)
    
    # assign num1 and/or num2 depending on how many numbers entered
    if to_len > 2:
        num1 = float(my_str_to[1])
        num2 = float(my_str_to[2])
    elif to_len == 2:
        num1 = float(my_str_to[1])
    
    

    if fun == 'q':
        break
    
    elif fun == '+':
        result = add(num1, num2)
        
    elif fun == '-':
        result = subtract(num1, num2)

        
    elif fun == '*':
        result = multiply(num1, num2)
    elif fun == '/':
        result = divide(num1, num2)
    elif fun == 'square':
        result = square(num1)
    elif fun == 'cube':
        result = cube(num1)
    elif fun == 'pow':
        result = power(num1, num2)
    elif fun == 'mod':
        result = mod(num1, num2)
    
    print(result)
        


        



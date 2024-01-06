# Class 1: intro of python and contextual info

Command line (Linux)

- ">" overwrite
- ">>" append

Python

1. main block:

        if __name__ == '__main__':
            #  __name__ is a built-in variable which evaluates to the name of the current module (i.e. not the name 'main.py')
            # __name__ is __main__ when the script is executed directly, not imported

2. function:

        def func_name(input1, input2, input3=5):
            return 5

notably: 
- if no return in function, the function will return None
- return also means the end of the function (usually used in for loops)
- the inputs with default values (input3=5) must be at the end of argument list

3. types:

    3.1 when casting float into int, only the integer part will be kept

    3.2 when casting float/int into bool, 0 is false, others are true

    3.3 when casting string into bool, '' is false, others are true

    3.4 str is in fact a list of characters

    3.5 when casting charactors into int (vice versa), reference to ASCII code, standard format for python is decimal

4. Conditions and Conditional Statements

    4.1 Conditions operators: and, or, not, symbols (==, !=, <, <=, >, >=)

    4.2 Conditional statements

    - if/elif/else 
    - while

        while vs for:

            while is followed up by a condition directly, and for needn't

5. List

    5.1 Indexing

    - Starts from 0
    - -1 stands for the last

    5.2 Slicing

        list[a:b] means list[a] to list[b-1]
        list[a:b:c] means list[a] to list[b-1], with a step of c (default 1).
        when c is negative, take inversly (need to invert a and b)

    5.3 append

        it returns nothing but None, only use it when the operation is inplace.




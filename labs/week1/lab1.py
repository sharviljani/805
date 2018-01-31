"""
Sharvil jani
UNHM COMP805 Lab 1
An Introduction to Python
Jan 29, 2018

The purpose of this file is to learn BASIC python syntax and data structures.
There is an accompanying test file. Place both files in the same directory,
and then run:
$ python tests.py

You will see a print out of tests that are being run, and your result.
Please see: https://www.python.org/dev/peps/pep-0008/ for style guidelines
"""

def give_me_a_string():
    """
    This function returns a string value
    """
    result = "My Name Is Sharvil Jani!!"
    return result
    pass

def give_me_an_integer():
    """
    This function returns an integer value
    """
    result = 10
    return result
    pass

def give_me_a_boolean():
    """
    This function returns a boolean value
    """
    a = 3
    b = 8
    result = a + b
    if result >10:
        return True
    else:
        return False
    pass

def give_me_a_float():
    """
    This function returns a float value
    """
    a = 1.4
    b = 4.8
    result = a + b
    return result
    pass

def give_me_a_list():
    """
    This function returns a list
    """
    a = []
    return a
    pass

def give_me_a_dictionary():
    """
    This function returns a dictionary
    """
    a_dict = {'sdj' : 26, 'ap' : 23}
    return a_dict
    pass

def give_me_a_tuple():
    """
    This function returns a tuple
    """
    birth_date = (14 , 'August' , 1992)
    return birth_date
    pass

def sum_numbers_one_to_ten():
    """
    This function returns the sum of all numbers one to ten
    Use the range function:
    https://docs.python.org/3/library/functions.html
    Use the accumulator pattern:
    http://interactivepython.org/runestone/static/thinkcspy/Functions/TheAccumulatorPattern.html
    """
    Sum = 0
    for x in range(1 , 11): # This will give us the range from 1 to 10
        Sum = Sum + x
    return Sum

    pass

def check_is_even(number):
    """
    This function returns True if num is even
    else False
    hint: use modulo operator
    https://docs.python.org/3/reference/expressions.html
    """
    if number % 2 == 0:
        return True 
    else:
        return False
    pass

def check_is_less_than(number1, number2):
    """
    This functions returns True if number1 < number2
    else False
    """

    if number1 < number2:
        return True
    else:
        return False
    pass

def check_is_equal_to(number1 , number2):
    """
    This function returns True if number1 == number2
    else False
    """
    
    if number1 == number2:
        return True
    else:
        return False
    pass

def product_one_to_ten():
    """
    This function returns the product of all numbers one to ten
    Use the range function:
    https://docs.python.org/3/library/functions.html
    Use the accumulator pattern:
    http://interactivepython.org/runestone/static/thinkcspy/Functions/TheAccumulatorPattern.html
    """
    product = 1
    for x in range(1 , 11): # This will give us the range from 1 to 10
        product = product * x
    return product



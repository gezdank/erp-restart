""" Common module
implement commonly used functions here
"""

import random


def generate_random(table):
    """
    Generates random and unique string. Used for id/key generation:
         - at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letter
         - it must be unique in the table (first value in every row is the id)

    Args:
        table (list): Data table to work on. First columns containing the keys.

    Returns:
        string: Random and unique string
    """

    generated = ''

    letters = "abcdefghijklmnopqrstuvwxyz"
    capitals = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    symbols = "&#"

    while True:
        for i in range(1):
            generated += letters[random.randint(0,26)]
        for i in range(1):
            generated += capitals[random.randint(0,26)]
        for i in range(2):
            generated += str(random.randint(0,9))
        for i in range(1):
            generated += capitals[random.randint(0,26)]
        for i in range(1):
            generated += letters[random.randint(0,26)]
        for i in range(2):
            generated += symbols[random.randint(0,2)]
            

    # your code

    return generated

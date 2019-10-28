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

def search_max(list_):
    """ Search for the maximum value in a dictionary
    Returns the key of the maximum value """
    max_ = [0, 0]
    for i, l in enumerate(list_):
        if l[1] > max_[1]:
            max_[1] = l[1]
            max_[0] = l[0]
    return max_[0]

def check_inputs(inputs, types, restrictions = [[]]):
    ''' Checks the input by types and restrictions
    args:
        types(list), example: ["int", "str"]
        restrictions(list), example: [0, 11], ["a", "b"]'''
    inputs_ = []
    try:
        for x, i in enumerate(inputs):
            if types[x] == "int":
                inputs_.append(int(i))
            elif types[x] == "str":
                inputs_.append(str(i))
    except:
        return False

    #rint(inputs_)

    if not restrictions:
        print(restrictions)
        for x, i in enumerate(inputs_):
            #TODO
            if types[x] == "int":
                if len(restrictions[x]) == 2:
                    if i < restrictions[x][0] or i > restrictions[x][1]:
                        return False
                elif len(restrictions[x]) == 1:
                    if i < restrictions[x][0]:
                        return False
            if types[x] == "str":
                if i in [restrictions[x]]:
                    return False

    return True
    #if inputs[0] > 0 and inputs[0] < 13:
        
def alphabetical_order(table, ids, ID, value):
    names = {}

    for row in table:
        if row[ID] in ids:
            names[row[ID]] = row[value]

    name = max(names.items(), key=lambda x: x[1])   #TODO an own algorithm

    return name[0]
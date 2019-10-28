""" User Interface (UI) module """


def print_table(table, title_list):
    """
    Prints table with data.

    Example:
        /-----------------------------------\
        |   id   |      title     |  type   |
        |--------|----------------|---------|
        |   0    | Counter strike |    fps  |
        |--------|----------------|---------|
        |   1    |       fo       |    fps  |
        \-----------------------------------/

    Args:
        table (list): list of lists - table to display
        title_list (list): list containing table headers

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    # your goes code

    width_titles = []
    for title in title_list:
        width_titles.append(len(title))
    sum_lenght = 0
    for j in range(len(title_list)):
        for i in table:
            if len(str(i[j])) > width_titles[j]:
                width_titles[j] = len(str(i[j]))
    for i in range(len(width_titles)):
        width_titles[i] += 2
        sum_lenght += width_titles[i] + 1
    sum_line = "-" * (sum_lenght-1)  
    just_line = ("|" + sum_line + "|")
    end_line = ("\\" + sum_line + "/")
    print("/" + sum_line + "\\")
    print("|", end ="")
    for index in range(len(title_list)):
        print((title_list[index]).center(width_titles[index]) + "|",end="")
    print()
    print(just_line)
    for i in range(len(table)):
        print("|",end="")
        for j in range(len(title_list)):
            print(((str(table[i][j])).center(width_titles[j])) + "|",end="")
        print()
        if i+1 == len(table):
            print(end_line)
        else:
            print(just_line)

def print_result(result, label):
    """
    Displays results of the special functions.

    Args:
        result: result of the special function (string, number, list or dict)
        label (str): label of the result

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    # your code
    print(label)
    if type(result) is str or type(result) is int or type(result) is float:
        print(result)
    elif type(result) is list:
        for item in result:
            print(item)
    elif type(result) is dict:
        for key in result:
            print(str(key) + " : " + str(result[key]))

def print_menu(title, list_options, exit_message):
    """
    Displays a menu. Sample output:
        Main menu:
            (1) Store manager
            (2) Human resources manager
            (3) Inventory manager
            (4) Accounting manager
            (5) Sales manager
            (6) Customer relationship management (CRM)
            (0) Exit program

    Args:
        title (str): menu title
        list_options (list): list of strings - options that will be shown in menu
        exit_message (str): the last option with (0) (example: "Back to main menu")

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    # your code
    print(title)
    index = 1
    for row in list_options:
        print(chr(9) + "(" + str(index) + ") " + row)
        index += 1
    print(chr(9) + "(0) " + exit_message)
    
def get_inputs(list_labels, title):
    """
    Gets list of inputs from the user.
    Sample call:
        get_inputs(["Name","Surname","Age"],"Please provide your personal information")
    Sample display:
        Please provide your personal information
        Name <user_input_1>
        Surname <user_input_2>
        Age <user_input_3>

    Args:
        list_labels (list): labels of inputs
        title (string): title of the "input section"

    Returns:
        list: List of data given by the user. Sample return:
            [<user_input_1>, <user_input_2>, <user_input_3>]
    """
    inputs = []

    # your code

    print(title)
    for index in range(len(list_labels)):
        inputs.append(input(list_labels[index]))
    return inputs

def print_error_message(message):
    """
    Displays an error message (example: ``Error: @message``)

    Args:
        message (str): error message to be displayed

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    # your code
    print("``Error: " + message + "``")
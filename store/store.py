""" Store module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game
    * manufacturer (string)
    * price (number): Price in dollars
    * in_stock (number)
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common

ID = 0
TITLE = 1
MANUFACTURER = 2
PRICE = 3
STOCK = 4 


def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """
    table = data_manager.get_table_from_file("store/games.csv")

    options = ["Add a new game",
               "Remove a game",
               "Show all games",
               "Update game store",
               "Check stock by Manufacturer",
               "Show all games averages by Manufacturer"]

    while True:
        ui.print_menu("Game Store", options, "Return to main menu")
        inputs = ui.get_inputs(["Choose an option: "], "")
        option = inputs[0]
        if option == "1":
            add(table)
            data_manager.write_table_to_file("store/games.csv", table)
        elif option == "2":
            inputs = ui.get_inputs(["Add ID of a game: "], "")
            remove(table,inputs[0])
            data_manager.write_table_to_file("store/games.csv", table)
        elif option == "3":
            show_table(table)
        elif option == "4":
            inputs = ui.get_inputs(["Enter game ID: "], "")
            update(table, inputs[0])
            data_manager.write_table_to_file("games.csv", table)
        elif option == "5":
            inputs = ui.get_inputs(["Enter Manufacturer: "], "")
            get_counts_by_manufacturers(table,inputs[0])
        elif option == "6":
            get_average_by_manufacturer(table,inputs[0])
        elif option == "0":
            break
        else:
            raise KeyError("There is no such option.")

    # your code


def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """
    
    ui.print_table(table, ["ID", "TITLE", "MANUFACTURER", "PRICE", "STOCK"])
    # your code


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    # your code
    row = []
    row.append(common.generate_random(table))

    inputs = ui.get_inputs(["TITLE: ", "MANUFACTURER: ", "PRICE: ", "STOCK: "], "Fill the records below: ")
    for i in inputs:
        row.append(i)

    table.append(row)

    return table



def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table (list): table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        list: Table without specified record.
    """

    # your code
    for i, row in enumerate(table):
        if row[ID] == id_:
            table.pop(i)
            return table

    ui.print_error_message("Wrong ID!")

    return table

    return table


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table: list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """

    # your code

    return table


# special functions:
# ------------------

def get_counts_by_manufacturers(table):
    """
    Question: How many different kinds of game are available of each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
         dict: A dictionary with this structure: { [manufacturer] : [count] }
    """

    # your code


def get_average_by_manufacturer(table, manufacturer):
    """
    Question: What is the average amount of games in stock of a given manufacturer?

    Args:
        table (list): data table to work on
        manufacturer (str): Name of manufacturer

    Returns:
         number
    """

    # your code

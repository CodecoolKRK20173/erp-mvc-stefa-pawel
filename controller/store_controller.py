# everything you'll need is imported:
from model.store import store
from view import terminal_view
from controller import common


def run():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    # your code

    list_options = ["1. Add new record to table", 
                    "2. Remove a record with a given id from the table", 
                    "3. Update specified record in the table", 
                    "4. How many different kinds of game are available of each manufacturer?", 
                    "5. What is the average amount of games in stock of a given manufacturer?"]

    table = store.get_table()                                   # DLA KADEGO MODUŁU OSOBNO
    title_list = ["ID", "TITLE", "MANUFACTURER", "PRICE (in $)", "IN STOCK"]
    terminal_view.print_table(table, title_list)
    
    answer = terminal_view.get_choice(list_options)

    if answer == "1":
        record = ["1", "2", "3", "4", "5", "6"]
        store.add(table, record)
        accounting.save_table(table)
    elif answer == "2":
        id_ = ""
        store.remove(table, id_)
    elif answer == "3":
        store.update(table, id_, record)
    elif answer =="4":
        store.get_counts_by_manufacturers(table)
    elif answer == "5":
        store.get_average_by_manufacturer(table, manufacturer)
    #elif answer == "0":
        #exit to main menu
    return 

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


    list_options = ["1. Add new record to table", 
                    "2. Remove a record with a given id from the table", 
                    "3. Update specified record in the table", 
                    "4. How many different kinds of game are available of each manufacturer?", 
                    "5. What is the average amount of games in stock of a given manufacturer?"]

    
    program_works = True

    while program_works:
        table = store.get_table()
        title_list = ["ID", "TITLE", "MANUFACTURER", "PRICE (in $)", "IN STOCK"]
        terminal_view.print_table(table, title_list)
        
        answer = terminal_view.get_choice(list_options)

        if answer == "1":
            record = terminal_view.get_inputs(["ID: ","Title of the game: ","Manufacturer: ","Price in dollars: ","In stock (number): "],"Please provide information: \n")
            common.add(table, record)
            store.save_table(table)
        elif answer == "2":
            id_ = terminal_view.get_input("Please enter id number: ")
            common.remove(table, id_)
            store.save_table(table)
        elif answer == "3":
            id_ = terminal_view.get_input("Please enter id number: ")
            record = terminal_view.get_inputs(["ID: ","Title of the game: ","Manufacturer: ","Price in dollars: ","In stock (number): "],"Please provide information: \n")
            common.update(table, id_, record)
            store.save_table(table)
        elif answer =="4":
            store.get_counts_by_manufacturers(table)
        elif answer == "5":
            store.get_average_by_manufacturer(table, manufacturer)
        elif answer == "0":
            program_works = False
        else:
            terminal_view.print_error_message("There is no such choice. Choose from 1 to 5")
    return 

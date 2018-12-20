# everything you'll need is imported:
from view import terminal_view
from model.sales import sales
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
                    "4. What is the id of the item that was sold for the lowest price?", 
                    "5. Which items are sold between two given dates?"]
    
    program_works = True

    while program_works:
        table = sales.get_table()  
        title_list = ["ID", "TITLE", "PRICE","MONTH","DAY","YEAR"]
        terminal_view.print_table(table, title_list)

        answer = terminal_view.get_choice(list_options)

        if answer == "1":
            record = terminal_view.get_inputs(["ID: ","Title of the game sold: ","The actual sale price in USD: ","Month of the sale: ","Day of the sale: ","Year of the sale: "],"Please provide information: \n")
            common.add(table, record)
            sales.save_table(table)
        elif answer == "2":
            id_ = terminal_view.get_input("Please enter id number: ")
            common.remove(table, id_)
            sales.save_table(table)
        elif answer == "3":
            id_ = terminal_view.get_input("Please enter id number: ")
            record = terminal_view.get_inputs(["ID: ","Title of the game sold: ","The actual sale price in USD: ","Month of the sale: ","Day of the sale: ","Year of the sale: "],"Please provide information: \n")
            common.update(table, id_, record)
            sales.save_table(table)
        elif answer == "4":
            sales.get_oldest_person(table)
        elif answer == "5":
            sales.get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to)
        elif answer == "0":
            program_works = False
        else:
            terminal_view.print_error_message("There is no such choice. Choose from 1 to 5")
    return 

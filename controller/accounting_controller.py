# everything you'll need is imported:
from view import terminal_view
from model.accounting import accounting
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
                    "4. Which year has the highest profit?", 
                    "5. What is the average (per item) profit in a given year?"]
    
    program_works = True
    while program_works:
   
        table = accounting.get_table()  
        title_list = ["ID", "MONTH", "DAY", "YEAR", "TYPE", "AMOUNT"]
        terminal_view.print_table(table, title_list)

        answer = terminal_view.get_choice(list_options)

        if answer == "1":
            record = terminal_view.get_inputs(["ID: ","Month of the transaction: ","Day of the transaction: ", "Year of the transaction: ", "Type - income/outflow (in.out): ", "Amount of transaction in USD: "],"Please provide information: \n")
            common.add(table, record)
            accounting.save_table(table)
        elif answer == "2":
            id_ = terminal_view.get_input("Please enter id number: ")
            common.remove(table, id_)
            accounting.save_table(table)
        elif answer == "3":
            id_ = terminal_view.get_input("Please enter id number: ")
            record = terminal_view.get_inputs(["ID: ","Month: ","Day: ", "Year: ", "Type: ", "Ammount: "],"Please provide new information")
            common.update(table, id_, record)
            accounting.save_table(table)
        elif answer =="4":
            accounting.which_year_max(table)
        elif answer == "0":
            program_works = False
        else:
            terminal_view.print_error_message("There is no such choice. Choose from 1 to 5")
    return 

    
    

    


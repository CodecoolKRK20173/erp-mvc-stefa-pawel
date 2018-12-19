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
    list_options = ["1. add", "2. remove", "3. update", "4. max year", "5. exit menu"]
    
    
    '''rysowanie tabeli''' 
    table = accounting.get_table()  
    title_list = ["ID", "MONTH", "DAY", "YEAR", "TYPE", "AMOUNT"]
    terminal_view.print_table(table, title_list)
    answer = terminal_view.get_choice(list_options)

    if answer == "1":
        #record = ["1", "2", "3", "4", "5", "6"]
        record = terminal_view.get_inputs(["ID","Month","Day", "Year", "Type", "Ammount"],"Please provide information")
        accounting.add(table, record)
        accounting.save_table(table)
    elif answer == "2":
        id_ = terminal_view.get_input("Please enter id number: ")
        accounting.remove(table, id_)
        accounting.save_table(table)
    elif answer == "3":
        accounting.update(table, id_, record)
    elif answer =="4":
        accounting.which_year_max(table)
    #elif answer == "5":
        #powrót do main menu - jak to zrobic?
    return 

    
    

    


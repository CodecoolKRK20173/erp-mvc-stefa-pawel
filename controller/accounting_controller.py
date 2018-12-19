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
<<<<<<< HEAD
    list_options = ["1. add", "2. remove", "3. update", "4. max year", "5. exit menu"]
    
    
    '''rysowanie tabeli''' 
    table = accounting.get_table()  
    title_list = ["ID", "MONTH", "DAY", "YEAR", "TYPE", "AMOUNT"]
    terminal_view.print_table(table, title_list)
    answer = terminal_view.get_choice(list_options)

    if answer == "1":
        #record = ["1", "2", "3", "4", "5", "6"]
        record = terminal_view.get_inputs(["ID","Month","Day", "Year", "Type", "Ammount"],"Please provide information")
=======
    #print_menu("Acounting menu", list_options, "Exit program") nie potrzebne bo printuje get_choice 

    list_options = ["1. Add new record to table", 
                    "2. Remove a record with a given id from the table", 
                    "3. Update specified record in the table", 
                    "4. Which year has the highest profit?", 
                    "5. What is the average (per item) profit in a given year?"]

    table = accounting.get_table()                                   # DLA KADEGO MODUŁU OSOBNO
    title_list = ["ID", "MONTH", "DAY", "YEAR", "TYPE", "AMOUNT"]
    terminal_view.print_table(table, title_list)
    
    answer = terminal_view.get_choice(list_options)

    if answer == "1":
        record = ["1", "2", "3", "4", "5", "6"]
>>>>>>> 640fd90db26e43e696db098f276862183c68ae3a
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
    #elif answer == "0":
        #powrót do main menu - jak to zrobic?
    return 

<<<<<<< HEAD
    
    

    
=======

>>>>>>> 640fd90db26e43e696db098f276862183c68ae3a


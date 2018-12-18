# everything you'll need is imported:
from view import terminal_view
from model.accounting import accounting
from controller import common

list_options = ["1. add", "2. remove", "3. update", "4. max year", "5. exit menu"]


def run():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """
    #print_menu("Acounting menu", list_options, "Exit program") nie potrzebne bo printuje get_choice 
    terminal_view.get_choice(list_options)
    answer = get_choice(list_options)

    if answer == "1":
        accounting.add(table, record)
    elif answer == "2":
        accounting.remove(table, id_)
    elif answer == "3":
        accounting.update(table, id_, record)
    elif answer =="4":
        accounting.which_year_max(table)
    #elif answer == "5":
        #powrót do main menu - jak to zrobic?
    return 

<<<<<<< HEAD
    # your code
    table = accounting.get_table()                                   # DLA KADEGO MODUŁU OSOBNO
    title_list = ["ID", "MONTH", "DAY", "YEAR", "TYPE", "AMOUNT"]
    terminal_view.print_table(table, title_list)

    record = ["1", "2", "3", "4", "5", "6"]
    accounting.add(table, record)
    # print("\n\n", table, "\n\n")
    accounting.save_table(table)

=======
>>>>>>> 701c46be0eb9297316684bd1fa64234856cd12a4

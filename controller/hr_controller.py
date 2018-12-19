# everything you'll need is imported:
from view import terminal_view
from model.hr import hr
from controller import common

def run():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    list_options = ["1. add", "2. remove", "3. update", "4. get oldest"]
    #tutaj prosimy o input użytkownika
    
    '''rysowanie tabeli''' 
    table = hr.get_table()  
    title_list = ["ID", "NAME", "DATE OF BIRTH"]
    terminal_view.print_table(table, title_list)

    answer = terminal_view.get_choice(list_options)

    if answer == "1":
        record = terminal_view.get_inputs(["ID","Name and surname","Date of birth"],"Please provide your personal information")
        hr.add(table, record)
        hr.save_table(table)
    elif answer == "2":
        id_ = terminal_view.get_input("Please enter id number: ")
        hr.remove(table, id_)
        hr.save_table(table)
    elif answer == "3":
        hr.update(table, id_, record)
    elif answer =="4":
        hr.get_oldest_person(table)
    #elif answer == "5":
        #powrót do main menu - jak to zrobic?
    return 


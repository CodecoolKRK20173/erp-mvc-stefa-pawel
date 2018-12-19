# everything you'll need is imported:
from view import terminal_view
from model.crm import crm
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
                    "4. What is the id of the customer with the longest name?", 
                    "5. Which customers has subscribed to the newsletter?"]
    
    
    '''rysowanie tabeli''' 
    table = crm.get_table()  
    title_list = ["ID", "NAME", "EMAIL", "SUBSCRIBED? y/n",]
    terminal_view.print_table(table, title_list)
    answer = terminal_view.get_choice(list_options)

    if answer == "1":
        record = terminal_view.get_inputs(["ID: ","Name: ","E-mail: ", "Subscription? Yes/ No"],"Please provide information: \n")
        crm.add(table, record)
        crm.save_table(table)
    elif answer == "2":
        id_ = terminal_view.get_input("Please enter id number: ")
        crm.remove(table, id_)
        crm.save_table(table)
    elif answer == "3":
        crm.update(table, id_, record)
    elif answer =="4":
        crm.get_longest_name_id(table)
    elif answer =="5":
        crm.get_subscribed_emails(table)
    #elif answer == "0":
        #powrót do main menu - jak to zrobic?
    return 

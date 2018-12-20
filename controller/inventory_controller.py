# everything you'll need is imported:
from view import terminal_view
from model.inventory import inventory
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
                    "4. Which items have not exceeded their durability yet?", 
                    "5. What are the average durability times for each manufacturer?"]
    
    
    program_works = True

    while program_works:
        table = inventory.get_table()  
        title_list = ["ID", "NAME", "MANUFACTURER","PURCHASE YEAR","DURABILITY"]
        terminal_view.print_table(table, title_list)

        answer = terminal_view.get_choice(list_options)

        if answer == "1":
            record = terminal_view.get_inputs(["ID: ","Name: ","Manufacturer: ","Purchase year: ","Durability: " ],"Please provide information: \n")
            common.add(table, record)
            inventory.save_table(table)
        elif answer == "2":
            id_ = terminal_view.get_input("Please enter id number: ")
            common.remove(table, id_)
            inventory.save_table(table)
        elif answer == "3":
            id_ = terminal_view.get_input("Please enter id number: ")
            record = terminal_view.get_inputs(["Enter ID: ","Name of item: ", "Manufacturer: ", "Year of purchase", "Durability year"],"Please provide new information")
            common.update(table, id_, record)
            inventory.save_table(table)
        elif answer =="4":
            inventory.get_oldest_person(table)
        elif answer == "5":
            inventory.get_average_durability_by_manufacturers(table)
        elif answer == "0":
            program_works = False
        else:
            terminal_view.print_error_message("There is no such choice. Choose from 1 to 5")
    return

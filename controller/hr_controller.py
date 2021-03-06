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

    list_options = ["1. Add new record to table", 
                    "2. Remove a record with a given id from the table", 
                    "3. Update specified record in the table",
                    "4. Which person is oldest",
                    "5. Which person is closest to average"]
    

    program_works = True

    while program_works:
        table = hr.get_table()  
        title_list = ["ID", "NAME", "DATE OF BIRTH"]
        terminal_view.print_table(table, title_list)
        answer = terminal_view.get_choice(list_options)

        if answer == "1":
            record = terminal_view.get_inputs(["ID: ","Name and surname: ","Date of birth: "],"Please provide your personal information")
            common.add(table, record)
            hr.save_table(table)
        elif answer == "2":
            id_ = terminal_view.get_input("Please enter id number: ")
            common.remove(table, id_)
            hr.save_table(table)
        elif answer == "3":
            id_ = terminal_view.get_input("Please enter id number: ")
            record = terminal_view.get_inputs(["ID: ","Name and surname: ", "Year of birth: "],"Please provide new information")
            common.update(table, id_, record)
            hr.save_table(table)
        elif answer =="4":
            print(hr.get_oldest_person(table))
            # result = hr.get_oldest_person(table)
            # terminal_view.print_result(result, "Oldest person is: ")
        elif answer == "5":
            hr.get_persons_closest_to_average(table)
        elif answer == "0":
            program_works = False
        else:
            terminal_view.print_error_message("There is no such choice. Choose from 1 to 5")
    return 


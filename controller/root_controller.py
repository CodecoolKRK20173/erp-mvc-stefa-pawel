# everything you'll need is imported:
from view import terminal_view
from controller import store_controller
from controller import hr_controller
from controller import inventory_controller
from controller import accounting_controller
from controller import sales_controller
from controller import crm_controller
from controller import common

#tu stworzyc main menu
def run():
<<<<<<< HEAD
    # options = ["Store manager",
    #            "Human resources manager",
    #            "Inventory manager",
    #            "Accounting manager",
    #            "Sales manager",
    #            "Customer Relationship Management (CRM)"]

    # choice = None
    # while choice != "0":
    #     choice = terminal_view.get_choice(options)
    #     if choice == "1":
    #         store_controller.run()
=======
    
    options = ["1. Store manager",
               "2. Human resources manager",
               "3. Inventory manager",
               "4. Accounting manager",
               "5. Sales manager",
               "6. Customer Relationship Management (CRM)"]

    choice = None
    while choice != "0":
        choice = terminal_view.get_choice(options)
        if choice == "1":
            store_controller.run()
>>>>>>> 701c46be0eb9297316684bd1fa64234856cd12a4
    #     elif choice == "2":
    #         hr_controller.run()
    #     elif choice == "3":
    #         inventory_controller.run()
<<<<<<< HEAD
    #     elif choice == "4":
    #         accounting_controller.run()
=======
        elif choice == "4":
            accounting_controller.run()
>>>>>>> 701c46be0eb9297316684bd1fa64234856cd12a4
    #     elif choice == "5":
    #         sales_controller.run()
    #     elif choice == "6":
    #         crm_controller.run()
    #     else:
    #         terminal_view.print_error_message("There is no such choice.")
<<<<<<< HEAD
    accounting_controller.run()
=======
    return

>>>>>>> 701c46be0eb9297316684bd1fa64234856cd12a4

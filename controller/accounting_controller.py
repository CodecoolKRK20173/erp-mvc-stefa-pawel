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

    # your code
    table = accounting.get_table()                                   # DLA KADEGO MODUŁU OSOBNO
    title_list = ["ID", "MONTH", "DAY", "YEAR", "TYPE", "AMOUNT"]
    terminal_view.print_table(table, title_list)

    record = ["1", "2", "3", "4", "5", "6"]
    accounting.add(table, record)
    # print("\n\n", table, "\n\n")
    accounting.save_table(table)


""" Human resources module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * birth_year (number)
"""

# everything you'll need is imported:
from model import data_manager
from model import common

def get_table():  
    table = data_manager.get_table_from_file("/home/stefania/Desktop/current week/erp-mvc-stefa-pawel/model/hr/persons_test.csv")
    return table


def save_table(table):
    data_manager.write_table_to_file("/home/stefania/Desktop/current week/erp-mvc-stefa-pawel/model/hr/persons_test.csv", table)


def add(table, record):
    """
    Add new record to table

    Args:
        table (list): table to add new record to
        record (list): new record

    Returns:
        list: Table with a new record
    """
    table = table.append(record)
    return table


def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table (list): table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        list: Table without specified record.
    """
    
    for lists in table:
        if id_ in lists:
            table = table.remove(lists)
    return table


def update(table, id_, record):
    """
    Updates specified record in the table.

    Args:
        table: list in which record should be updated
        id_ (str): id of a record to update
        record (list): updated record

    Returns:
        list: table with updated record
    """

    for lists in table:
        if id_ in lists:
            table.remove(lists)
            table.append(record)
    return table


# special functions:
# ------------------

def get_oldest_person(table):
    """
    Question: Who is the oldest person?

    Args:
        table (list): data table to work on

    Returns:
        list: A list of strings (name or names if there are two more with the same value)
    """
    years = []  # działa ale nie ma print_result w terminal view
    for lists in table:
        years.append(int(lists[2]))
        oldest_person = min(years)
    for lists in table:
        if oldest_person == int(lists[2]):
            return lists[1]
    


def get_persons_closest_to_average(table):
    """
    Question: Who is the closest to the average age?

    Args:
        table (list): data table to work on

    Returns:
        list: list of strings (name or names if there are two more with the same value)
    """

    # your code

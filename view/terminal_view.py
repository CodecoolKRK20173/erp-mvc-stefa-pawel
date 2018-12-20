""" Terminal view module """


def print_table(table, title_list):
    """
    Prints table with data.

    Example:
        /-----------------------------------\
        |   id   |      title     |  type   |
        |--------|----------------|---------|
        |   0    | Counter strike |    fps  |
        |--------|----------------|---------|
        |   1    |       fo       |    fps  |
        \-----------------------------------/

    Args:
        table (list): list of lists - table to display
        title_list (list): list containing table headers

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    # your goes code
    data = [title_list] + table
    longest_line_length = 0
    for i, d in enumerate(data):
        line = '|'.join(str(x).center(15) for x in d)
        line_length = len(line)

        if line_length > longest_line_length:
            longest_line_length = line_length
            longest_line = line
            max_i = i
        longest_element = max(data[max_i], key=len)
        longest_element_len = len(longest_element)
        longest_index = data[max_i].index(longest_element)

    for i, d in enumerate(data):
        line = '|'.join(str(x).center(15) for x in d)
        if d[longest_index]:
            line = '|'.join(str(x).center(longest_element_len) for x in d)
        dashes = len(line)
        if i == 0:
            print("/", '-' * dashes, "\\")

        if i == len(data) - 1:
            print("|", line, "|")
            print("\\", '-' * dashes, "/")
        else:
            print("|", line, "|")
            print("|", '-' * dashes, "|")
    longest_element_len = 0


def print_result(result, label):
    """
    Displays results of the special functions.

    Args:
        result: result of the special function (string, list or dict)
        label (str): label of the result

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    # your code


def print_menu(title, list_options, exit_message):
    """
    Displays a menu. Sample output:
        Main menu:
            (1) Store manager
            (2) Human resources manager
            (3) Inventory manager
            (4) Accounting manager
            (5) Sales manager
            (6) Customer relationship management (CRM)
            (0) Exit program

    Args:
        title (str): menu title
        list_options (list): list of strings - options that will be shown in menu
        exit_message (str): the last option with (0) (example: "Back to main menu")

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    print(title)
    for options in list_options:
        print(options)
    print(exit_message)
    return



def get_inputs(list_labels, title):  #return list of elements
    """                              działa!
    Gets list of inputs from the user.
    Sample call:
        get_inputs(["Name","Surname","Age"],"Please provide your personal information")
    Sample display:
        Please provide your personal information
        Name <user_input_1>
        Surname <user_input_2>
        Age <user_input_3>

    Args:
        list_labels (list): labels of inputs
        title (string): title of the "input section"

    Returns:
        list: List of data given by the user. Sample return:
            [<user_input_1>, <user_input_2>, <user_input_3>]
    """
    
    inputs = []
    print(title)
    for element in list_labels:
        answer = input(element)
        inputs.append(answer)
    return inputs


def get_input(question):  #return one object (str or int)
    answer = input(question)
    return answer


def get_choice(options):  #return one int, only to menu
    print_menu("Main menu",options, "0. Exit")
    inputs = get_inputs(["Please enter a number: "], "")
    return inputs[0]

def print_error_message(message):
    """
    Displays an error message (example: ``Error: @message``)
    Args:
        message (str): error message to be displayed
    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    print(message)
    

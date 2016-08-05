def create_menu(options, fail_method, cancel_method):
    """ Creates a numbers menu of options,
    and either returns a user's selection
    or executes a method if the user's input is invalid

    Method arguments:
    -----------------
    options(list) -- The list of options that will make up the menu choices
    fail_method(method reference) -- The method to be executed if a user makes an invalid input
    cancel_method(method reference) --  The method to be executed if a user inputs 'cancel'
    """
    selected_option = None
    i = 1
    # creates a menu using all users that currently exist
    for option in options:
        print("{}. {}".format(i, option))
        i += 1

    user_input = input("> ")

    if user_input.lower() == "quit":
        print("\nYou chose quit\n")
        quit()

    elif user_input.lower() == 'cancel':
        print("\nYou chose cancel")
        cancel_method()

    try:
        # if the user inputs an integer
        selected_index = int(user_input) - 1
        # and if the integer is in the range of number of options to select from
        if selected_index < len(options):
            # set the selected option based on the options list's index
            selected_option = options[selected_index]

    except ValueError:
        for option in options:
            # if the input is in one of the available options,
            if user_input.lower() in option.lower():
                # set that option as the selected option
                selected_option = option

    if selected_option is None:
        print("Invalid input, please try again\n")
        fail_method()

    return selected_option

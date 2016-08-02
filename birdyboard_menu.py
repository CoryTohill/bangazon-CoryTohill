import birdyboard


class BirdyBoardMenu():

    def __init__(self):
        self.board = birdyboard.BirdyBoard()

        print("Welcome to BirdyBoard!")

        self.show_main_menu()

    def show_main_menu(self):
        main_menu_options = {
            '1 New User Account': self.show_new_user_inputs,
            '2 Select User': self.show_user_select_menu,
            '3 View Chirps': self.show_chirps_menu,
            '4 Make a Chirp': self.show_create_a_chirp_menu
        }
        options_comp = [key for key in sorted(main_menu_options)]
        # ordered list of main_menu_options without the numbers used for ordering them
        formatted_options_comp = [option[2:] for option in options_comp]

        print("")
        print("Please choose an option below,")
        print("or type 'quit' at any time to leave the program:")
        print("")

        user_selection = self.create_menu(formatted_options_comp)

        if user_selection is not None:
            # displays the option the user selected
            print("You chose {}".format(user_selection))
            print("")

            index = formatted_options_comp.index(user_selection)

            # calls the corresponding function in main_menu_options based on user's input
            main_menu_options[options_comp[index]]()

        else:
            self.input_error_message()
            self.show_main_menu()

    def show_new_user_inputs(self):
        print("Enter full name:")
        full_name = input("> ")

        print("")

        print("Enter screen name:")
        screen_name = input("> ")

        # creates a new user and then returns to the main menu
        self.board.new_user(screen_name, full_name)
        print("")
        print(
            "Successfully created account for, and logged in as {}"
            .format(self.board.current_user['screen_name'])
        )

        self.show_main_menu()

    def show_user_select_menu(self):
        # makes a list of available screen names
        screen_name_comp = [user['screen_name'] for user in self.board.users]

        print("Select a user profile:")
        # makes a menu using all screen names as options to choose from
        selected_user_screen_name = self.create_menu(screen_name_comp)

        if selected_user_screen_name is not None:
            # gets index of selected user in screen_name_comp
            index = screen_name_comp.index(selected_user_screen_name)
            # uses the index to set the correct user to be the current user
            self.board.set_current_user(self.board.users[index])

        else:
            self.input_error_message()
            self.show_user_select_menu()

        print(
            "You are now logged in as {}"
            .format(self.board.current_user['screen_name'])
        )

        self.show_main_menu()



    def show_chirps_menu(self):
        private_chirps = []
        current_user_id = self.board.current_user['user_id']
        i = 1

        print("<< Public Chirps >>")
        for chirp in self.board.chirps:
            if chirp['is_private'] is False:
                print("{}. {}".format(i, chirp['message']))
                i += 1

            else:
                private_chirps.append(chirp)

        print("<< Private Chirps >>")
        for chirp in private_chirps:
            if (
                chirp['author'] == current_user_id or
                chirp['chirped_at_user_id'] == current_user_id
            ):
                print("{}. {}".format(i, chirp['message']))
                i += 1

        self.show_main_menu()



    def show_create_a_chirp_menu(self):
        selected_option = None
        is_private = False
        chirped_at_user_id = None
        create_a_chirp_menu_options = [
            "1. Public",
            "2. Private"
        ]

        print("This chirp will be:")
        # loops through and displays each option in create_a_chirp_menu_options
        for option in create_a_chirp_menu_options:
            print(option)

        user_input = input("> ")

        # if the user's input is any part of one of the options,
        # that options index value is saved as the selected_option
        for option in create_a_chirp_menu_options:
            if user_input.lower() in option.lower():
                selected_option = create_a_chirp_menu_options.index(option)

        # display error message and re-show menu if user's input was invalid
        if selected_option is None:
            self.input_error_message()
            self.show_create_a_chirp_menu()

        # display the option selected by the user
        print("")
        print(
            "You chose to make a {} chirp"
            .format(create_a_chirp_menu_options[selected_option][3:])
        )

        # if user selects pivate chirp, prompt for which user to chirp at
        if selected_option == 1:
            is_private = True

            # user selects which user they want to chirp at
            print("Chirp at:")
            selected_user = self.create_menu()

            if selected_user is not None:
                chirped_at_user_id = selected_user['user_id']

            else:
                self.show_create_a_chirp_menu()

        print("Enter chirp text:")
        message = input("> ")

        # creates the chirp based on user input
        self.board.create_chirp(message, is_private, chirped_at_user_id)

        print("")
        print("Chirp created!")

        self.show_main_menu()

    def create_menu(self, options):
        selected_option = None
        i = 1
        # creates a menu using all users that currently exist
        for option in options:
            print("{}. {}".format(i, option))
            i += 1

        user_input = input("> ")
        print("")

        if user_input.lower() == "quit":
            print("You chose quit")
            print("")
            quit()

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

        return selected_option

    def input_error_message(self):
        print("Invalid input, please try again")
        print("")

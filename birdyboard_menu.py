import birdyboard


class BirdyBoardMenu():

    def __init__(self):
        self.board = birdyboard.BirdyBoard()

        print("Welcome to BirdyBoard!")

        self.show_main_menu()

    def show_main_menu(self):
        main_menu_options = {
            '1 New User Account': self.create_new_user,
            '2 Select User': self.view_user_select_menu,
            '3 View Public Chirps': self.view_public_chirps_menu,
            # '4 View Private Chirps': self.view_private_chirps_menu,
            '5 Make a Chirp': self.create_a_chirp_menu
        }
        # sorted list of keys from main_menu_options
        options_comp = [key for key in sorted(main_menu_options)]
        # sorted list of main_menu_options without the numbers used for sorting them
        formatted_options_comp = [option[2:] for option in options_comp]

        print("")
        print("Please choose an option below,")
        print("or type 'quit' at any time to leave the program:")
        print("")

        user_selection = self.create_menu(formatted_options_comp, self.show_main_menu)

        # displays the option the user selected
        print("You chose {}".format(user_selection))
        print("")

        index = formatted_options_comp.index(user_selection)

        # calls the corresponding function in main_menu_options based on user's input
        main_menu_options[options_comp[index]]()

    def create_new_user(self):
        print("Enter full name:")
        full_name = input("> ")

        print("")

        print("Enter screen name:")
        screen_name = input("> ")

        # creates a new user and then returns to the main menu
        self.board.create_user(full_name, screen_name)
        print("")
        print(
            "Successfully created account for, and logged in as {}"
            .format(self.board.current_user.screen_name)
        )

        self.show_main_menu()

    def view_user_select_menu(self):
        # makes a list of available screen names
        screen_names = [user.screen_name for user in self.board.users.values()]

        print("Select a user profile:")
        # makes a menu using all screen names as options to choose from
        selected_screen_name = self.create_menu(screen_names, self.view_user_select_menu)

        # gets the key for the selected user by comparing
        # the selected screen name with all available screen names
        selected_user_key = next((key for key, value in self.board.users.items()
                             if value.screen_name == selected_screen_name))

        # sets the current user to the user selected
        self.board.set_current_user(self.board.users[selected_user_key])

        print(
            "You are now logged in as {}"
            .format(self.board.current_user.screen_name)
        )

        self.show_main_menu()


    def view_public_chirps_menu(self):
        # makes a list of all public messages
        public_chirps = [chirp for chirp in self.board.chirps.values()
                         if chirp.private is False
                         ]



        # # combines the public_chirps list and
        # # chirp_author_screen_names list to be the correct format for displaying chirps
        # for index in range(0, len(public_chirps)):
        #     chirp_menu_options.append(
        #         "{}: {}".format(
        #             chirp_author_screen_names[index],
        #             public_chirps[index].message
        #         )
        #     )

        # selected_public_message = self.create_menu(chirp_menu_options, self.view_public_chirps_menu)

        # message_index = chirp_menu_options.index(selected_public_message)

        # selected_chirp = public_chirps(message_index)



        # # # matches the selected chirp message to the correct chirp in the list of all chirps
        # # selected_chirp = next((chirp for chirp in self.board.chirps
        # #                        if chirp.message == selected_public_message
        # #                        ), None)


        # self.show_main_menu()

    def reply_to_chirp(self, message, user_id, conversation_id, private=False, receiver_id=None):
        self.board.create_chirp(message, user_id, private, receiver_id, conversation_id)
# **********************************************************************************************************
# **********************************************************************************************************
# **********************************************************************************************************

    def create_a_chirp_menu(self):
        type_of_chirp_options = [
            "Public",
            "Private"
        ]

        # forces users to log in before making a chirp
        if self.board.current_user is None:
            print("Error: Must be logged in to create a chirp!")
            self.show_main_menu()

        print("This chirp will be:")
        # creates menu with type_of_chirp_options as choices
        selected_type = self.create_menu(type_of_chirp_options, self.create_a_chirp_menu)

        print("")
        print(
            "You chose to make a {} chirp"
            .format(selected_type)
        )
        print("")

        # asks user who they want to chirp at before creating the new chirp
        if selected_type == "Private":
            screen_names = [user.screen_name for user in self.board.users.values()]

            print("Select a user to chirp at:")
            # makes a menu using all screen names as options to choose from
            selected_screen_name = self.create_menu(screen_names, self.create_a_chirp_menu)

            # loops through all users and gets the key associated with the users selection
            selected_user_key = next((key for key, value in self.board.users.items()
                                if value.screen_name == selected_screen_name))


            print(
                "You chose to chirp at {}"
                .format(self.board.users[selected_user_key].screen_name)
            )
            print("")

            print("Enter chirp text:")
            message = input("> ")

            self.board.create_chirp(message, self.board.current_user.user_id, True, selected_user_key)

        # creates a public chirp
        else:
            print("Enter chirp text:")
            message = input("> ")

            self.board.create_chirp(message, self.board.current_user.user_id)



        print("")
        print("Chirp created!")

        self.show_main_menu()

    def create_menu(self, options, fail_method):
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

        if selected_option is None:
            self.input_error_message()
            fail_method()

        return selected_option

    def input_error_message(self):
        print("Invalid input, please try again")
        print("")

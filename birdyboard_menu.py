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
            # '3 View Chirps': self.show_public_chirps,
            '4 Make a Chirp': self.show_create_a_chirp_menu
        }
        # sorted list of keys from main_menu_options
        options_comp = [key for key in sorted(main_menu_options)]
        # sorted list of main_menu_options without the numbers used for sorting them
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
        self.board.create_user(full_name, screen_name)
        print("")
        print(
            "Successfully created account for, and logged in as {}"
            .format(self.board.current_user.screen_name)
        )

        self.show_main_menu()

    def show_user_select_menu(self):
        # makes a list of available screen names
        screen_names = [user.screen_name for user in self.board.users]

        print("Select a user profile:")
        # makes a menu using all screen names as options to choose from
        selected_screen_name = self.create_menu(screen_names)

        if selected_screen_name is not None:
            # gets index of selected user in screen_name_comp
            index = screen_names.index(selected_screen_name)
            # uses the index to set the correct user to be the current user
            self.board.set_current_user(self.board.users[index])

        else:
            self.input_error_message()
            self.show_user_select_menu()

        print(
            "You are now logged in as {}"
            .format(self.board.current_user.screen_name)
        )

        self.show_main_menu()


    # def show_public_chirps(self):
#         private_chirps = []
#         current_user_id = self.board.current_user['user_id']
#         i = 1
#         # list of all public chirps
#         public_chirps = [chirp for chirp in self.board.chirps if chirp['is_private'] == False]

#         print("<< Public Chirps >>")
#         self.create_menu(public_chirps)


    # def show_private_chirps(self):
#         current_user_id = self.board.current_user['user_id']
#         private_chirps = []

#         for chirp in self.board.chirps:
#             # is the chirp private
#             if chirp['is_private']:
#                 # is the chirp authored by or sent to the current user
#                 if (
#                     chirp['author'] == current_user_id or
#                     chirp['chirped_at_user_id'] == current_user_id
#                 ):
#                     # add chirp to private chirps list
#                     private_chirps.append(chirp)

#         print("<< Private Chirps >>")
#         self.create_menu(chirp['message'] for chirp in private_chirps)
#         self.show_main_menu()



    def show_create_a_chirp_menu(self):
        selected_option = None
        chirped_at_user_id = None
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
        selected_type = self.create_menu(type_of_chirp_options)

        print("")
        print(
            "You chose to make a {} chirp"
            .format(selected_type)
        )
        print("")

        # asks user who they want to chirp at before creating the new chirp
        if selected_type == "Private":
            screen_names = [user.screen_name for user in self.board.users]

            print("Select a user to chirp at:")
            # makes a menu using all screen names as options to choose from
            selected_screen_name = self.create_menu(screen_names)

            if selected_screen_name is not None:
                user_index = screen_names.index(selected_screen_name)
                receiver = self.board.users[user_index]

                print(
                    "You chose to chirp at {}"
                    .format(receiver.screen_name)
                )
                print("")

            else:
                self.input_error_message()
                self.show_create_a_chirp_menu()

            print("Enter chirp text:")
            message = input("> ")

            self.board.create_chirp(message, self.board.current_user.user_id, True, receiver.user_id)

        # creates a public chirp
        elif selected_type == "Public":
            print("Enter chirp text:")
            message = input("> ")

            self.board.create_chirp(message, self.board.current_user.user_id)

        else:
            self.input_error_message()
            self.show_create_a_chirp_menu()

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

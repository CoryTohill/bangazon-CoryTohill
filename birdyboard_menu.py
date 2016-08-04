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
            '3 View Public Chirps': self.view_chirps_menu,
            '4 View Private Chirps': self.view_private_chirps_menu,
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

        # displays the main menu
        user_selection = self.create_menu(formatted_options_comp,
                                          self.show_main_menu)

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
        selected_screen_name = self.create_menu(screen_names,
                                                self.view_user_select_menu)

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

    def view_chirps_menu(self, private=False):
        chirp_menu_options = []
        initial_chirps_ids = []

        # will make a list of either all private or public that are the beginning of a conversation
        for chirp_id_list in self.board.conversations.values():
            if self.board.chirps[chirp_id_list[0]].private == private:
                initial_chirps_ids.append(chirp_id_list[0])

        # will filter out any private chrips that are not authored by or sent to the current user
        if private is True:
            initial_chirps_ids = [chirp_id for chirp_id in initial_chirps_ids
                                  if self.board.chirps[chirp_id].author == self.board.current_user.user_id or
                                  self.board.chirps[chirp_id].receiver == self.board.current_user.user_id]

        # formats the data to so it will display with
        # the author of each chirp's screen name before the chirp message
        for chirp_id in initial_chirps_ids:
            current_chirp = self.board.chirps[chirp_id]
            current_chirp_author = self.board.users[current_chirp.author]

            chirp_menu_options.append("{}: {}".format(
                current_chirp_author.screen_name,
                current_chirp.message)
            )

        print("Select a chirp to view it's thread")
        print("or type 'cancel' to return to the main menu:")
        selected_chirp_menu_option = self.create_menu(chirp_menu_options,
                                                      self.view_chirps_menu)

        # splits the menu option on the first occurance of ": " and selects everything after it
        # which is the original chirp message
        selected_message = selected_chirp_menu_option.split(": ", 1)[1]

        # gets the id of the chirp the message belongs to
        selected_chirp_id = next((chirp.chirp_id for chirp in self.board.chirps.values()
                                  if chirp.message == selected_message))

        # gets the id of the conversation the chirp belongs to
        selected_conversation_id = next((key for key, chirp_list
                                        in self.board.conversations.items()
                                        if chirp_list[0] == selected_chirp_id))

        # displays the chirp thread
        self.show_chirp_thread(selected_conversation_id, self.board.chirps[selected_chirp_id])

    def view_private_chirps_menu(self):
        self.view_chirps_menu(private=True)

    def show_chirp_thread(self, conversation_id, original_chirp):

        # gets all chirps in the conversation that was passed in
        chirps_to_show = [self.board.chirps[chirp_id]
                          for chirp_id
                          in self.board.conversations[conversation_id]]

        # print chirp messages and users
        for chirp in chirps_to_show:
            print("{}: {}".format(self.board.users[chirp.author].screen_name,
                                  chirp.message))

        print("")
        print("Select an option:")
        print("1. Reply")
        print("2. Cancel")
        user_input = input("> ")
        print("")

        # Cancel option returns to the main menu
        if user_input.lower() in "2. cancel":
            self.show_main_menu()

        # Reply option will prompt for a chirp message,
        # then create a new chirp and add it to the conversation
        elif user_input.lower() in "1. reply":
            print("Enter chirp text:")
            message = input("> ")
            print("")

            self.board.create_chirp(message,
                                    self.board.current_user.user_id,
                                    original_chirp.private,
                                    conversation_id=conversation_id)

        else:
            print("Invalid input, please try again.")
            print("")

        # re-shows the current menu
        self.show_chirp_thread(conversation_id, original_chirp)

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
        selected_type = self.create_menu(type_of_chirp_options,
                                         self.create_a_chirp_menu)

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
            selected_screen_name = self.create_menu(screen_names,
                                                    self.create_a_chirp_menu)

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

            self.board.create_chirp(message,
                                    self.board.current_user.user_id,
                                    True,
                                    selected_user_key)

        # creates a public chirp
        else:
            print("Enter chirp text:")
            message = input("> ")

            self.board.create_chirp(message,
                                    self.board.current_user.user_id)

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

        elif user_input.lower() == 'cancel':
            print("You chose cancel")
            self.show_main_menu()

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

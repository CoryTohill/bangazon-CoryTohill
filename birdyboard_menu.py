import birdyboard


class BirdyBoardMenu():

    def __init__(self):
        self.board = birdyboard.BirdyBoard()

        print("Welcome to BirdyBoard!")
        print("")

        self.show_main_menu()

    def show_main_menu(self):
        main_menu_options = {
            '1. New User Account': self.show_new_user_inputs,
            '2. Select User': self.show_user_select_menu,
            '3. View Chirps': self.show_chirps_menu,
            '4. Public Chirp': self.show_chirp_inputs,
            '5. Private Chirp': self.show_private_chirp_user_menu
        }

        print("Please choose an option below,")
        print("or type 'exit' to leave the program:")
        print("")

        # prints all keys in main_menu_options
        for key in sorted(main_menu_options):
            print(key)

        main_menu_input = input("> ")

        # exits the program if user enters exit
        if main_menu_input.lower() == "exit":
            quit()

        # if the user input is in one of the keys in the main_menu_dict
        # the main_menu_input is redifined to be that key
        for key in main_menu_options:
            if main_menu_input in key:
                main_menu_input = key

        # displays the option the user selected
        print("You chose {}".format(main_menu_input[3:]))
        print("")

        # calls the appropriate function in main_menu_options based on user's input
        main_menu_options[main_menu_input]()

    def show_new_user_inputs(self):
        print("Enter full name:")
        full_name = input("> ")

        print("Enter screen name:")
        screen_name = input("> ")

        # creates a new user and returns to the main menu
        self.board.new_user(screen_name, full_name)
        self.show_main_menu()

    def show_user_select_menu(self):
        print("Select a user profile:")
        i = 1

        # creates a menu using all users that currently exist
        for user in self.board.users:
            print("{}. {}".format(i, user['screen_name']))
            i += 1

        self.show_main_menu()

    def show_chirps_menu(self):
        print("show chirps menu")
        self.show_main_menu()

    def show_chirp_inputs(self):
        print("show chirps inputs")
        self.show_main_menu()

    def show_private_chirp_user_menu(self):
        print("show private chirp user menu")
        self.show_main_menu()

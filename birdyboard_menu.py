import birdyboard


class BirdyBoardMenu():

    def __init__(self):
        self.board = birdyboard.BirdyBoard()

        print("Welcome to BirdyBoard!")
        print("")

        self.show_main_menu()

    def show_main_menu(self):
        main_menu_options = [
            '1. New User Account',
            '2. Select User',
            '3. View Chirps',
            '4. Public Chirp',
            '5. Private Chirp',
        ]
        print("Please choose an option below,")
        print("or type 'exit' to leave the program:")
        print("")

        for option in main_menu_options:
            print(option)

        main_menu_input = input("> ")

        if main_menu_input.lower() == "exit":
            quit()

    def show_new_user_inputs(self):
        pass

    def show_user_select_menu(self):
        pass

    def show_chirps_menu(self):
        pass

    def show_chirp_inputs(self):
        pass

    def show_private_chirp_user_menu(self):
        pass

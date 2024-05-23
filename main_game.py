from crown_of_axum import CrownOfAksum
from book_of_enoch import BookOfEnoch
from Configer import Configer
from SoundBox import SoundBox
from AsciiArt import AsciiArt
from colorama import init, Fore, Style

class Game:
    def __init__(self):
        self.configer = Configer()
        self.soundbox = SoundBox()
        self.ascii_art = AsciiArt()
        self.score = 0
        self.user_name = ""
        init(autoreset=True)  # Initialize colorama

    def start(self):
        # Load game content
        self.load_game_content()

        # Start background music
        self.soundbox.start_background_music(self.configer.get_setting("background_music"))

        # Get user name
        self.user_name = input(Fore.CYAN + "Enter your name: ")

        # Introduction
        print(Fore.GREEN + f"Welcome to the Ethiopia Exploration Adventure, {self.user_name}!")

        # Main game loop
        while True:
            user_input = input(Fore.YELLOW + "Would you like to explore Ethiopia? (yes/no): ").lower()
            if user_input == "no":
                print(Fore.RED + f"Thank you for playing, {self.user_name}! Goodbye!")
                break
            elif user_input == "yes":
                self.choose_adventure()
            else:
                print(Fore.RED + "Invalid input. Please enter 'yes' or 'no'.")

    def load_game_content(self):
        # Load sounds
        self.soundbox.load_sound("game_over", self.configer.get_setting("game_over_sound"))
        self.soundbox.set_narrator_voice(self.configer.get_setting("narrator_voice"))

    def choose_adventure(self):
        print(Fore.MAGENTA + "Choose an adventure to explore:")
        print(Fore.MAGENTA + "1. The Crown of Aksum")
        print(Fore.MAGENTA + "2. The Book of Enoch")
        print(Fore.MAGENTA + "3. New Adventure")
        print(Fore.MAGENTA + "4. Quit")

        while True:
            choice = input(Fore.CYAN + "Enter the number of your chosen adventure: ")
            if choice == "1":
                self.ascii_art.crown_of_axum()
                crown_adventure = CrownOfAksum()
                crown_adventure.start(self)
                break
            elif choice == "2":
                self.ascii_art.book_of_enoch()
                book_adventure = BookOfEnoch()
                book_adventure.start(self)
                break
        print(Fore.RED + "Game Over!")
        self.soundbox.play_sound("game_over")
        print(Fore.YELLOW + f"Your final score: {self.score}")

    def update_score(self, points):
        self.score += points
        print(Fore.CYAN + f"Your current score: {self.score}")

if __name__ == "__main__":
    game = Game()
    game.start()

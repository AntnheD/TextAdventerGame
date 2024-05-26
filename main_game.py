from Configer import Configer
from SoundBox import SoundBox
from AsciiArt import AsciiArt
from crown_of_axum import CrownOfAksum
from book_of_enoch import BookOfEnoch
from colorama import init, Fore
import time

class Game:
    def __init__(self):
        self.configer = Configer()
        self.soundbox = SoundBox()
        self.ascii_art = AsciiArt()
        self.score = 0
        self.user_name = ""
        self.rooms = ["Addis Ababa", "Aksum", "Gondar", "Hidden Chamber", "Monk's Chamber", "Holy Trinity Church"]
        self.room_descriptions = {
            "Addis Ababa": "You find yourself in the bustling streets of Addis Ababa.",
            "Aksum": "You arrive at St. Mary of Zion, the oldest church.",
            "Gondar": "You find yourself in the ancient city of Gondar, known for its castles.",
            "Hidden Chamber": "You find a hidden chamber filled with ancient artifacts.",
            "Monk's Chamber": "You encounter a wise monk who will test your knowledge of Ethiopia.",
            "Holy Trinity Church": "You stand before the Holy Trinity Church, seeking the book keeper."
        }
        self.room_connections = {
            "Addis Ababa": ["Aksum", "Gondar"],
            "Aksum": ["Addis Ababa", "Hidden Chamber"],
            "Gondar": ["Addis Ababa", "Hidden Chamber", "Monk's Chamber"],
            "Hidden Chamber": ["Aksum", "Gondar"],
            "Monk's Chamber": ["Gondar", "Holy Trinity Church"],
            "Holy Trinity Church": ["Monk's Chamber"]
        }
        self.game_state = {
            "crown_found": False,
            "puzzle_solved": False,
            "monk_quiz_passed": False,
            "book_found": False
        }
        self.questions = [
            {"question": "What is the capital of Ethiopia?", "answer": "Addis Ababa"},
            {"question": "In which city is the St. Mary of Zion located?", "answer": "Aksum"},
            {"question": "Which Ethiopian emperor is known for modernizing the country?", "answer": "Haile Selassie"},
            {"question": "What is the main language spoken in Ethiopia?", "answer": "Amharic"},
            {"question": "What is the highest mountain in Ethiopia?", "answer": "Ras Dashen"},
            {"question": "Which lake is the source of the Blue Nile?", "answer": "Lake Tana"},
            {"question": "What is the ancient script used in Ethiopia?", "answer": "Ge'ez"},
            {"question": "Which Ethiopian city is famous for its rock-hewn churches?", "answer": "Lalibela"},
            {"question": "What is the traditional Ethiopian bread called?", "answer": "Injera"},
            {"question": "Which festival celebrates the finding of the True Cross in Ethiopia?", "answer": "Meskel"}
        ]
        init(autoreset=True)  # Initialize colorama

    def start(self):
        # Load game content
        self.load_game_content()

        # Start background music
        self.soundbox.start_background_music(self.configer.get_setting("background_music"))
        # Start welcome ascii
        self.ascii_art.welcome()
        # Get user name
        self.user_name = input(Fore.CYAN + "Enter your name: ")

        # Introduction
        print(Fore.GREEN + f"Welcome to the Ethiopia Exploration Adventure, {self.user_name}!")

        # Main game loop
        current_room = "Addis Ababa"  # Start in Addis Ababa
        while True:
            print(Fore.YELLOW + self.room_descriptions[current_room])
            user_input = input(Fore.YELLOW + "Would you like to explore further? (yes/no): ").lower()
            if user_input == "no":
                print(Fore.RED + f"Thank you for playing, {self.user_name}! Goodbye!")
                self.game_over()
                break
            elif user_input == "yes":
                current_room = self.choose_next_room(current_room)
            else:
                print(Fore.RED + "Invalid input. Please enter 'yes' or 'no'.")

    def load_game_content(self):
        # Load sounds
        self.soundbox.load_sound("game_over", self.configer.get_setting("game_over_sound"))
        self.soundbox.set_narrator_voice(self.configer.get_setting("narrator_voice"))

    def choose_next_room(self, current_room):
        print(Fore.MAGENTA + "You can go to the following rooms:")
        for i, room in enumerate(self.room_connections[current_room]):
            print(Fore.MAGENTA + f"{i + 1}. {room}")

        while True:
            choice = input(Fore.CYAN + "Enter the number of the room you want to go to: ")
            if choice.isdigit() and 1 <= int(choice) <= len(self.room_connections[current_room]):
                new_room = self.room_connections[current_room][int(choice) - 1]
                if new_room == "Aksum" and not self.game_state["crown_found"]:
                    crown_adventure = CrownOfAksum()
                    crown_adventure.start(self)
                    self.game_state["crown_found"] = True
                    print(Fore.GREEN + "You found the Crown of Aksum!")
                    self.ascii_art.crown_of_axum()
                elif new_room == "Hidden Chamber" and not self.game_state["puzzle_solved"]:
                    book_adventure = BookOfEnoch()
                    book_adventure.start(self)
                    self.game_state["puzzle_solved"] = True
                    print(Fore.GREEN + "You solved the puzzle and discovered the Book of Enoch!")
                    self.ascii_art.book_of_enoch()
                elif new_room == "Monk's Chamber" and not self.game_state["monk_quiz_passed"]:
                    self.start_monk_quiz()
                    if self.game_state["monk_quiz_passed"]:
                        print(Fore.GREEN + "You passed the monk's quiz!")
                    else:
                        self.game_over()
                        break
                elif new_room == "Holy Trinity Church" and not self.game_state["book_found"]:
                    self.ascii_art.book_of_enoch()
                    book_adventure = BookOfEnoch()
                    book_adventure.start(self)
                    self.game_state["book_found"] = True
                    print(Fore.GREEN + "You found the Book of Enoch in Holy Trinity Church!")
                return new_room
            else:
                print(Fore.RED + "Invalid choice. Please enter a valid room number.")

    def start_monk_quiz(self):
        print(Fore.BLUE + "The monk will now ask you 10 questions about Ethiopia.")
        correct_answers = 0
        for q in self.questions:
            answer = input(Fore.CYAN + q["question"] + " ")
            if answer.lower() == q["answer"].lower():
                correct_answers += 1
        if correct_answers >= 5:
            self.game_state["monk_quiz_passed"] = True
            self.update_score(50)
            print(Fore.GREEN + f"You answered {correct_answers} questions correctly!")
        else:
            print(Fore.RED + f"You answered only {correct_answers} questions correctly. It's not enough to pass.")
            self.game_over()

    def game_over(self):
        self.ascii_art.game_overe()  # Call the method with the correct name
        print(Fore.RED + "Game Over!")
        self.soundbox.play_sound("game_over")
        print(Fore.YELLOW + f"Your final score: {self.score}")
        time.sleep(10)  # Add a 10-second delay
        exit()

    def update_score(self, points):
        self.score += points
        print(Fore.CYAN + f"Your current score: {self.score}")

if __name__ == "__main__":
    game = Game()
    game.start()

class BookOfEnoch:
    def __init__(self):
        self.rooms = {
            "Gondar": {
                "description": "You find yourself in the historical city of Gondar, Ethiopia.",
                "options": {
                    "explore": "Travel to the Simien Mountains",
                    "examine": "Look around",
                    "quit": "Quit the adventure"
                }
            },
            "Simien Mountains": {
                "description": "You embark on a treacherous journey through the mountains.",
                "options": {
                    "enter": "Seek the monks' guidance",
                    "leave": "Leave the mountains"
                }
            },
            "Monastery": {
                "description": "You reach an ancient monastery hidden in the cliffs.",
                "options": {
                    "seek": "Seek the monks' guidance",
                    "leave": "Leave the monastery"
                }
            },
            "Hidden Chamber": {
                "description": "The Book of Enoch rests on an altar before you.",
                "options": {
                    "take": "Take the book",
                    "leave": "Leave it protected"
                }
            }
        }
        self.current_room = "Gondar"

    def start(self, game):
        print("Welcome to 'The Book of Enoch' text adventure!")
        while self.current_room:
            self.describe_room()
            choice = self.get_choice()
            self.process_choice(choice, game)

    def describe_room(self):
        room = self.rooms[self.current_room]
        print(room["description"])
        for action, description in room["options"].items():
            print(f"- {action.capitalize()}: {description}")

    def get_choice(self):
        return input("What will you do? ").strip().lower()

    def process_choice(self, choice, game):
        if choice == "explore" and self.current_room == "Gondar":
            self.current_room = "Simien Mountains"
        elif choice == "enter" and self.current_room == "Simien Mountains":
            self.current_room = "Monastery"
        elif choice == "seek" and self.current_room == "Monastery":
            self.current_room = "Hidden Chamber"
        elif choice == "take" and self.current_room == "Hidden Chamber":
            print("You have successfully retrieved the Book of Enoch!")
            game.update_score(10)
            self.current_room = None
        elif choice == "leave":
            if self.current_room == "Simien Mountains":
                self.current_room = "Gondar"
            elif self.current_room == "Monastery":
                self.current_room = "Simien Mountains"
            elif self.current_room == "Hidden Chamber":
                print("You decide to leave the book undisturbed.")
                game.update_score(5)
                self.current_room = None
        elif choice == "examine" and self.current_room == "Gondar":
            print("You hear rumors about an ancient monastery in the Simien Mountains.")
        elif choice == "quit":
            self.current_room = None
        else:
            print("Invalid choice. Try again.")

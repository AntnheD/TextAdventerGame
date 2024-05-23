class CrownOfAksum:
    def __init__(self):
        self.rooms = {
            "Addis Ababa": {
                "description": "You find yourself in the bustling streets of Addis Ababa.",
                "options": {
                    "explore": "Journey to Aksum",
                    "examine": "Look around",
                    "quit": "Quit the adventure"
                }
            },
            "Aksum": {
                "description": "You arrive at St. Mary of Zion, the oldest church.",
                "options": {
                    "enter": "Enter the hidden passage",
                    "leave": "Leave the church"
                }
            },
            "Hidden Passage": {
                "description": "You venture deeper into the tunnel.",
                "options": {
                    "decipher": "Decipher the ancient inscriptions",
                    "leave": "Leave the passage"
                }
            },
            "Hidden Chamber": {
                "description": "The Crown of Aksum rests on a pedestal before you.",
                "options": {
                    "claim": "Claim the crown",
                    "leave": "Leave it undisturbed"
                }
            }
        }
        self.current_room = "Addis Ababa"

    def start(self, game):
        print("Welcome to 'The Crown of Aksum' text adventure!")
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
        if choice == "explore" and self.current_room == "Addis Ababa":
            self.current_room = "Aksum"
        elif choice == "enter" and self.current_room == "Aksum":
            self.current_room = "Hidden Passage"
        elif choice == "decipher" and self.current_room == "Hidden Passage":
            self.current_room = "Hidden Chamber"
        elif choice == "claim" and self.current_room == "Hidden Chamber":
            print("You have successfully retrieved the Crown of Aksum!")
            game.update_score(10)
            self.current_room = None
        elif choice == "leave":
            if self.current_room == "Aksum":
                self.current_room = "Addis Ababa"
            elif self.current_room == "Hidden Passage":
                self.current_room = "Aksum"
            elif self.current_room == "Hidden Chamber":
                print("You decide to leave the crown undisturbed.")
                game.update_score(5)
                self.current_room = None
        elif choice == "examine" and self.current_room == "Addis Ababa":
            print("The map hints at Lalibela's rock-hewn churches. Perhaps they hold additional clues.")
        elif choice == "quit":
            self.current_room = None
        else:
            print("Invalid choice. Try again.")

import os
import pygame
import SoundBox
from AsciiArt import ASCIIArt
class Configer:
    def __init__(self):
        self.keywords = {
            "lalibela": {
                
                "artifacts": "lalibela_artifacts.txt",
                "church": "lalibela_church.txt",
                "mysteries": "lalibela_mysteries.txt",
                "goto": ["gondar"]
            },
            "axum": {
                "artifacts": "axum_artifacts.txt",
                "ark": "axum_ark.txt",
                "legacy": "axum_legacy.txt",
                "goto": ["simien"]
            },
            "gondar": {
                "castle": "gondar_castle.txt",
                "secrets": "gondar_secrets.txt",
                "royal": "gondar_royal.txt",
                "goto": ["lalibela", "axum"]
            },
            "simien": {
                "mountains": "simien_mountains.txt",
                "wildlife": "simien_wildlife.txt",
                "expedition": "simien_expedition.txt",
                "goto": ["axum"]
            }
        }
        self.current_location = None
        self.soundbox = SoundBox()

    def set_location(self, location):
        """Sets the current game location."""
        if location in self.keywords:
            self.current_location = location
        else:
            raise ValueError("Invalid location specified.")

    def search_keywords_and_return_file(self, user_input):
        """
        Searches for keywords in the user input based on the current location and returns the corresponding text file.
        Also checks for "goto" keywords and changes location.

        Args:
        user_input (str): The string input from the user.

        Returns:
        str: The content of the corresponding text file, a message to change location, or an error message.
        """
        if not self.current_location:
            return "No location set. Please set the current location first."

        location_keywords = self.keywords.get(self.current_location, {})
        goto_locations = location_keywords.get("goto", [])

        for keyword in user_input.lower().split():  # Search individual words
            if keyword in location_keywords:
                return self.read_file(location_keywords[keyword])
            elif keyword in goto_locations:
                self.set_location(keyword)
                ascii_art_method = getattr(ASCIIArt, keyword, None)
                if ascii_art_method:
                    return  f"{ascii_art_method()}\nTraveling to {keyword}...\n" + self.search_keywords_and_return_file(user_input)  # Include ASCII art when traveling
                else:
                    return "no ascii art for this"
            elif keyword == "narrate":
                return self.narrate_specific_text(user_input)

        return "No matching keywords found for the current location."

    def read_file(self, filename):
        """
        Reads the content of a text file.

        Args:
        filename (str): The name of the text file to read.

        Returns:
        str: The content of the text file or an error message if the file does not exist.
        """
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                return file.read()
        else:
            return f"File {filename} does not exist."

    def narrate_specific_text(self, user_input):
        """Narrate specific text based on user input."""
        # Extract the specific text to narrate from the user input
        # For example, if user input is "narrate lalibela mysteries", narrate the mysteries of Lalibela
        specific_text = user_input.split("narrate ")[1].strip()

        # Map specific text to content
        text_content = {
            "lalibela mysteries": "Legend has it that Lalibela holds many mysteries waiting to be uncovered. From hidden chambers to secret passages, explorers have long been fascinated by the enigmatic aura surrounding this ancient city.",
            # Add more specific text mappings as needed
        }

        # Narrate the specific text if available
        if specific_text in text_content:
            self.soundbox.play_narrator(text_content[specific_text])
            return ""  # Return empty string as we don't want to display the text in the game interface
        else:
            return f"No specific text found for '{specific_text}'."

# Define the SoundBox class (provided in the previous message)

# Example usage
if __name__ == "__main__":
    configer = Configer()

    # Set the current location to Lalibela
    configer.set_location("lalibela")
    user_input = input("Enter your search keywords: ")
    result = configer.search_keywords_and_return_file(user_input)
    print(result)

    # Example of narrating specific text
    user_input = "narrate lalibela mysteries"
    result = configer.search_keywords_and_return_file(user_input)
    print(result)

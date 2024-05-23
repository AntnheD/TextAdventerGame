class Configer:
    def __init__(self):
        self.settings = self.load_settings()

    def load_settings(self):
        # Load settings from a file or define them here
        settings = {
            "background_music": "sounds/background_music.mp3",
            "game_over_sound": "sounds/game_over_sound.wav",
            "narrator_voice": "sounds/narrator_voice.wav",
            "score_increment": 10
        }
        return settings

    def get_setting(self, key):
        return self.settings.get(key, None)

    def set_setting(self, key, value):
        self.settings[key] = value

    def save_settings(self):
        # Save settings to a file if needed
        pass

# Example usage
if __name__ == "__main__":
    configer = Configer()
    print(configer.get_setting("background_music"))
    configer.set_setting("new_setting", "new_value")
    print(configer.get_setting("new_setting"))

class Configer:
    def __init__(self):
        self.settings = {
            "background_music": "sounds/background_music.mp3",
            "game_over_sound": "sounds/game_over_sound.mp3",
            "narrator_voice": "sounds/narrator_voice.wav"
        }

    def get_setting(self, key):
        return self.settings.get(key, None)

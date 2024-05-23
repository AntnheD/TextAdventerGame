import pygame

class SoundBox:
    def __init__(self):
        pygame.mixer.init()
        self.sounds = {}
        self.narrator_voice = None

    def load_sound(self, name, file_path):
        self.sounds[name] = pygame.mixer.Sound(file_path)

    def play_sound(self, name):
        if name in self.sounds:
            self.sounds[name].play()

    def set_narrator_voice(self, file_path):
        self.narrator_voice = pygame.mixer.Sound(file_path)

    def play_narrator_voice(self):
        if self.narrator_voice:
            self.narrator_voice.play()

    def start_background_music(self, file_path):
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play(-1)  # Loop the background music

    def stop_background_music(self):
        pygame.mixer.music.stop()

# Example usage
if __name__ == "__main__":
    soundbox = SoundBox()
    soundbox.load_sound("game_over", "game_over_sound.wav")
    soundbox.play_sound("game_over")

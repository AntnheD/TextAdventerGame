import pygame

class SoundBox:
    def __init__(self):
        pygame.mixer.init()
        self.sounds = {}
        self.narrator_voice = None

    def load_sound(self, name, file_path):
        self.sounds[name] = file_path

    def play_sound(self, name):
        if name in self.sounds:
            if name == "game_over":
                pygame.mixer.music.load(self.sounds[name])
                pygame.mixer.music.play()
            else:
                pygame.mixer.Sound(self.sounds[name]).play()

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

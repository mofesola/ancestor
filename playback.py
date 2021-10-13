import os, random
import pygame

class Playback:

    def get_file():
        return random.choice(os.listdir("sounds/"))
    
    def playsound():
        file_name = Playback.get_file() 
        Playback.pygame_play("sounds/" +file_name)

    def talk_to_me():
        Playback.pygame_play("config/audio/talk_to_me.mp3")

    def startup():
        Playback.pygame_play("config/audio/ancestors_listening.mp3")

    def pygame_play(file_name):
        print("Playing file " + file_name + "...")
        pygame.mixer.init()
        pygame.mixer.music.load(file_name)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue

if __name__ == "__main__":
    Playback.playsound()
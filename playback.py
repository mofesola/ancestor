#from playsound import playsound
import os, random
import pygame

class Playback:

    def get_file():
        return random.choice(os.listdir("sounds/"))
    
    def playsound():
        file_name = Playback.get_file() 
        print("Playing file " + file_name + "...")
        pygame.mixer.init()
        pygame.mixer.music.load("sounds/" + file_name)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
        #playsound("sounds/" + Playback.get_file())


if __name__ == "__main__":
    Playback.playsound()
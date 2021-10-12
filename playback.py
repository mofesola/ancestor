from playsound import playsound
import os, random
#import pygame

class Playback:

    def get_file():
        return random.choice(os.listdir("sounds/"))
    
    def playsound():
        file_name = Playback.get_file() 
        print("Playing file " + file_name + "...")
        playsound("sounds/" + file_name)
    
    def talk_to_me():
        playsound("sounds/talk_to_me.mp3")


if __name__ == "__main__":
    Playback.playsound()
from playsound import playsound
import os, random

class Playback:

    def get_file():
        return random.choice(os.listdir("sounds/"))
    
    def playsound():
        print("Playing file " + Playback.get_file() + "...")
        playsound("sounds/" + Playback.get_file())


import os
import random
from random import randint

def play_song():
    n = random.randint(0,10)
    print(n)
    music_dir = 'D:\sachin\music\audio.mp3'
    songs = os.listdir(music_dir)
    print(songs)
    os.startfile(os.path.join(music_dir,songs[n]))
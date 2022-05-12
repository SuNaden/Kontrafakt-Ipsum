import sys
from os import listdir
from os.path import isfile, join
from random import randrange

# Get a random song lyrics from /data
songs = [f for f in listdir('./data') if isfile(join('./data', f))]
random_song_path = './data/' + songs[randrange(len(songs))]

# Read the lyrics, split by whitespace
f = open(random_song_path, "r")
lyrics = f.read().lower().split()
f.close()

# Cut first {X} words
if (sys.argv[2]):
  lyrics_ipsum = lyrics[:int(sys.argv[2])]
else:
  sys.stdout.write("Kámo, ty čo robíš?")

sys.stdout.write(' '.join(lyrics_ipsum))
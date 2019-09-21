from gtts import gTTS as g
import os

fh = open('nolan.txt', 'r')
mytext = fh.read().replace('\n', ' ')

language = 'en'
output = g(text = mytext, lang = language, slow = False)
fh.close()
output.save('nolan.mp3')
# os.system('start output.mp3')

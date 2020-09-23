# from gtts import gTTS
# play = 'audio.mp3'
# language = 'ru'
#
# audio = gTTS(text = 'Перерыв на обед', lang = 'ru', slow = False)
#
# audio.save(play)
# playsound(audio)

#from gtts import gTTS
#from playsound import playsound
#play = 'audio.mp3'
#language = 'ru'

#audio = gTTS(text = 'Перерыв на обед', lang = 'ru', slow = False)

#audio.save(play)
#playsound(play)
from gtts import gTTS
from playsound import playsound
play = 'audio.mp3'
language = 'ru'

audio = gTTS('Hello. How are you? Good Day!', lang = 'ru', slow = False)
audio.save(play)
playsound(play)

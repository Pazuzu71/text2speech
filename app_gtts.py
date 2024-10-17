# Import the required module for text
# to speech conversion
from gtts import gTTS

name = '1.Numpy-intro'
# The text that you want to convert to audio
with open(f'{name}.txt', encoding='utf-8') as f:
    my_text = f.read()

# Language in which you want to convert
language = 'ru'

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
my_obj = gTTS(text=my_text, lang=language, slow=True)

# Saving the converted audio in a mp3 file named
# welcome
my_obj.save(f'{name}.mp3')

# Playing the converted file
# os.system("start welcome.mp3")

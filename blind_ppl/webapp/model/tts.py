from gtts import gTTS
import os
def text2speech(translated_text):
    tts = gTTS(translated_text)
    # tts.save('blind_ppl\webapp\static\audio\audio.mp3')
    tts.save('audio.mp3')
    
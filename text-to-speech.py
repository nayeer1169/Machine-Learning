#pip install pyttsx3

import pyttsx3
text_speech = pyttsx3.init()

answer = input("What you want to say ?\n")

text_speech.say(answer)
text_speech.runAndWait()
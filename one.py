import pyttsx3

# initialize
engine = pyttsx3.init()

text = """
Welcome to our project.
This script converts text into voice without any API key.
You can generate audio easily.
"""

engine.say(text)
engine.runAndWait()


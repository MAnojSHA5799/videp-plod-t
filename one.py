from google import genai
from google.genai import types
import base64

# Gemini API key
client = genai.Client(api_key="AIzaSyAt97skhphFdmhym3o0uLEBO8xKdeq0a6o")

text = """
Welcome to our project.
This script converts text into real human voice using Gemini AI.
You can generate high quality narration automatically.
"""

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=text,
    config=types.GenerateContentConfig(
        response_modalities=["AUDIO"]
    )
)

# extract audio
audio_data = response.candidates[0].content.parts[0].inline_data.data
audio_bytes = base64.b64decode(audio_data)

# save audio
with open("voice.wav", "wb") as f:
    f.write(audio_bytes)

print("✅ Voice generated successfully -> voice.wav")
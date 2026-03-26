from gtts import gTTS
import os
import tempfile

def speak(text):
    print(f"ARIA says: {text}")
    tts = gTTS(text=text, lang='en', slow=False)
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as f:
        tts.save(f.name)
        os.system(f"afplay {f.name}")

if __name__ == "__main__":
    speak("Hello! I am ARIA, your AI Robot Intelligence Assistant!")
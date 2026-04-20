import os
import tempfile

is_speaking = False


def speak(text: str) -> None:
    global is_speaking
    is_speaking = True
    print(f'ARIA: {text}')
    try:
        from gtts import gTTS
        with tempfile.NamedTemporaryFile(suffix='.mp3', delete=False) as f:
            tmp = f.name
        tts = gTTS(text=text, lang='en', slow=False)
        tts.save(tmp)
        os.system(f'mpg123 -q {tmp} 2>/dev/null')
        os.unlink(tmp)
    except Exception:
        # Fallback to espeak when gTTS / mpg123 is unavailable
        safe = text.replace('"', "'")
        os.system(f'espeak -s 145 "{safe}" 2>/dev/null')
    finally:
        is_speaking = False


if __name__ == '__main__':
    speak('Hello! I am ARIA, your AI Robot Intelligence Assistant!')
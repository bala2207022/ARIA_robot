import speech_recognition as sr

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("ARIA is listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source, timeout=10, phrase_time_limit=10)
    try:
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Couldn't understand audio")
        return None
    except sr.RequestError:
        print("Speech service unavailable")
        return None

if __name__ == "__main__":
    result = listen()
    print(f"Result: {result}")
import speech_recognition as sr
import time

STOP_WORDS = ['stop', 'exit', 'quit', 'bye', 'goodbye', 'shut down', 'sleep']


def listen(wait_after_speak: float = 1.5):
    """Capture one voice command and return it as lowercase text, or None."""
    recognizer = sr.Recognizer()
    recognizer.energy_threshold = 300
    recognizer.dynamic_energy_threshold = True
    recognizer.pause_threshold = 0.8

    # Try to find a working microphone (indices 0-4)
    mic = None
    for i in range(5):
        try:
            test = sr.Microphone(device_index=i)
            with test as s:
                recognizer.adjust_for_ambient_noise(s, duration=0.3)
            mic = test
            break
        except Exception:
            continue

    if mic is None:
        print("No microphone found")
        return None

    # Small pause so ARIA's own speech doesn't get picked up
    time.sleep(wait_after_speak)

    with mic as source:
        print('Listening…')
        try:
            audio = recognizer.listen(source, timeout=7, phrase_time_limit=8)
        except sr.WaitTimeoutError:
            return None

    try:
        text = recognizer.recognize_google(audio)
        print(f'You said: {text}')
        if any(w in text.lower() for w in STOP_WORDS):
            return 'stop'
        return text
    except sr.UnknownValueError:
        print('Could not understand')
        return None
    except sr.RequestError:
        print('Speech service unavailable')
        return None


if __name__ == '__main__':
    result = listen()
    print(f'Result: {result}')
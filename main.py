from voice.listener import listen
from voice.speaker import speak
from ai.assistant import ask_aria

def run_aria():
    speak("Hello! I am ARIA, your AI Robot Intelligence Assistant. How can I help you?")
    
    while True:
        print("\nListening for your command...")
        command = listen()
        
        if command is None:
            speak("I didn't catch that, please say it again!")
            continue
        
        if "stop" in command.lower() or "goodbye" in command.lower():
            speak("Goodbye! See you soon!")
            break
        
        print(f"Thinking about: {command}")
        response = ask_aria(command)
        speak(response)

if __name__ == "__main__":
    run_aria()
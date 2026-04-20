import time
import os
import threading

import RPi.GPIO as GPIO

from voice.listener import listen
from voice.speaker import speak, is_speaking
from ai.assistant import ask_aria
from face_recognition.recognize import load_known_faces, capture_frame, recognize_face
from face_recognition.train import train_face

# ── Pan-Tilt Servo Setup ──────────────────────────────────────────────────────
PAN_PIN  = 18   # GPIO 18 – Left / Right
TILT_PIN = 23   # GPIO 23 – Up / Down

pan_angle  = 90.0
tilt_angle = 60.0   # start tilted up (robot sits on the floor)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(PAN_PIN,  GPIO.OUT)
GPIO.setup(TILT_PIN, GPIO.OUT)

pan_pwm  = GPIO.PWM(PAN_PIN,  50)
tilt_pwm = GPIO.PWM(TILT_PIN, 50)
pan_pwm.start(0)
tilt_pwm.start(0)


def move_pan(angle):
    global pan_angle
    angle = max(0, min(180, float(angle)))
    if abs(angle - pan_angle) < 2:
        return
    pan_pwm.ChangeDutyCycle(2.5 + (angle / 180.0) * 10)
    time.sleep(0.15)
    pan_pwm.ChangeDutyCycle(0)
    pan_angle = angle


def move_tilt(angle):
    global tilt_angle
    angle = max(30, min(90, float(angle)))
    if abs(angle - tilt_angle) < 2:
        return
    tilt_pwm.ChangeDutyCycle(2.5 + (angle / 180.0) * 10)
    time.sleep(0.15)
    tilt_pwm.ChangeDutyCycle(0)
    tilt_angle = angle


def track_face_servo(face_x, face_y):
    """Nudge pan/tilt servos to keep the detected face centred (320×240 frame)."""
    global pan_angle, tilt_angle
    x_off = face_x - 160
    y_off = face_y - 120
    if abs(x_off) > 25:
        move_pan(pan_angle  - x_off * 0.04)
    if abs(y_off) > 20:
        move_tilt(tilt_angle + y_off * 0.04)


# ── State ─────────────────────────────────────────────────────────────────────
known_faces, known_names = load_known_faces()
last_greeted: dict = {}
GREET_COOLDOWN = 30   # seconds between repeated greetings
aria_busy = False
current_name = None   # person currently in front of ARIA


# ── Camera loop ───────────────────────────────────────────────────────────────
def scan_once():
    global aria_busy, current_name
    try:
        frame = capture_frame()
        if frame is None:
            return
        names, positions = recognize_face(frame, known_faces, known_names)
        if positions:
            # positions are (cx, cy) tuples
            cx, cy = positions[0]
            track_face_servo(cx, cy)
        for name in names:
            if name not in ("No face", "Unknown"):
                current_name = name
                now = time.time()
                if name not in last_greeted or (now - last_greeted[name]) > GREET_COOLDOWN:
                    aria_busy = True
                    speak(f"Hi {name}! Good to see you!")
                    last_greeted[name] = now
                    aria_busy = False
    except Exception as exc:
        print(f"Camera error: {exc}")


def camera_loop():
    print("Camera started…")
    while True:
        if not aria_busy:
            scan_once()
        time.sleep(5)


# ── Command handler ───────────────────────────────────────────────────────────
def handle_command(command: str) -> bool:
    """Process a voice command. Returns False to shut down ARIA."""
    global aria_busy, current_name
    if command is None:
        return True
    command = command.lower().strip()
    print(f"Command: {command}")

    if any(w in command for w in ("stop", "bye", "goodbye", "exit", "quit")):
        speak("Goodbye! See you soon!")
        return False

    if "who are you" in command or "your name" in command:
        speak("I am ARIA, your AI Robot Intelligence Assistant!")
        return True

    if any(p in command for p in ("train me", "remember me", "learn me")):
        speak("Sure! What is your name?")
        name = listen(wait_after_speak=1.0)
        if name and name.strip():
            train_face(name.strip().capitalize(), speak_fn=speak)
            known_faces[:], known_names[:] = zip(*[(kf, kn)
                for kf, kn in zip(*load_known_faces())]) if load_known_faces()[0] else ([], [])
        else:
            speak("Sorry, I did not catch your name. Please try again.")
        return True

    if "who am i" in command or "do you know me" in command:
        aria_busy = True
        frame = capture_frame()
        if frame is not None:
            names, _ = recognize_face(frame, known_faces, known_names)
            if names and names[0] not in ("No face", "Unknown"):
                speak(f"You are {names[0]}! I know you!")
            else:
                speak("I am not sure who you are. Say 'train me' so I can learn your face!")
        aria_busy = False
        return True

    if "weather" in command:
        try:
            from ai.weather import get_weather
            speak(get_weather())
        except Exception:
            speak("Sorry, I could not get the weather right now.")
        return True

    # ── Fallback: Claude AI ────────────────────────────────────────────────────
    try:
        response = ask_aria(command, recognized_name=current_name)
        speak(response)
    except Exception as exc:
        speak("Sorry, I could not get a response right now.")
        print(f"AI error: {exc}")
    return True


# ── Entry point ───────────────────────────────────────────────────────────────
def run_aria():
    speak("Hello! I am ARIA, your AI Robot Intelligence Assistant! I am ready!")
    cam_thread = threading.Thread(target=camera_loop, daemon=True)
    cam_thread.start()
    running = True
    while running:
        if aria_busy:
            time.sleep(0.5)
            continue
        print("\nListening…")
        command = listen()
        running = handle_command(command)
    speak("ARIA shutting down. Goodbye!")
    pan_pwm.stop()
    tilt_pwm.stop()
    GPIO.cleanup()


if __name__ == "__main__":
    run_aria()
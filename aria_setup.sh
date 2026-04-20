#!/bin/bash
# ARIA Full Setup Script - Run this on the Raspberry Pi
# Usage: bash /home/pi/aria_setup.sh

set -e
echo "=== ARIA Setup Starting ==="

# ---- Step 1: Install packages ----
echo "Installing packages..."
sudo apt-get install -y flac mpg123 python3-pyaudio libopenblas-dev 2>/dev/null || true
pip3 install gtts anthropic speechrecognition opencv-python playsound --break-system-packages 2>/dev/null || true
echo "Packages done."

# ---- Step 2: Write speaker.py ----
echo "Writing voice/speaker.py..."
cat > /home/pi/robot/voice/speaker.py << 'PYEOF'
from gtts import gTTS
import os
import tempfile

def speak(text):
    print(f"ARIA says: {text}")
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as f:
        tmpfile = f.name
    tts = gTTS(text=text, lang='en', slow=False)
    tts.save(tmpfile)
    os.system(f"mpg123 -q {tmpfile}")
    os.unlink(tmpfile)

if __name__ == "__main__":
    speak("Hello! I am ARIA, your AI Robot Intelligence Assistant!")
PYEOF

# ---- Step 3: Write listener.py ----
echo "Writing voice/listener.py..."
cat > /home/pi/robot/voice/listener.py << 'PYEOF'
import speech_recognition as sr

STOP_WORDS = ["stop", "exit", "quit", "bye", "goodbye", "shut down", "sleep"]

def listen():
    recognizer = sr.Recognizer()
    mic = sr.Microphone(device_index=0)
    with mic as source:
        print("ARIA is listening...")
        recognizer.energy_threshold = 300
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        try:
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=10)
        except sr.WaitTimeoutError:
            print("No speech detected")
            return None
    try:
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        if any(word in text.lower() for word in STOP_WORDS):
            return "stop"
        return text
    except sr.UnknownValueError:
        print("Could not understand")
        return None
    except sr.RequestError:
        print("Speech service unavailable")
        return None

if __name__ == "__main__":
    result = listen()
    print(f"Result: {result}")
PYEOF

# ---- Step 4: Write recognize.py ----
echo "Writing face_recognition/recognize.py..."
cat > /home/pi/robot/face_recognition/recognize.py << 'PYEOF'
import cv2
import pickle
import os
import numpy as np
import subprocess
import tempfile

def load_known_faces():
    known_faces = []
    known_names = []
    faces_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'known_faces')
    if not os.path.exists(faces_dir):
        os.makedirs(faces_dir)
        return known_faces, known_names
    for file in os.listdir(faces_dir):
        if file.endswith('.pkl'):
            with open(os.path.join(faces_dir, file), 'rb') as f:
                data = pickle.load(f)
                known_names.append(data['name'])
                known_faces.append(data['images'])
    return known_faces, known_names

def capture_frame():
    with tempfile.NamedTemporaryFile(suffix='.jpg', delete=False) as f:
        tmpfile = f.name
    subprocess.run([
        'rpicam-jpeg', '-o', tmpfile,
        '--timeout', '500', '-n',
        '--width', '640', '--height', '480',
        '--contrast', '1.2',
    ], capture_output=True)
    frame = cv2.imread(tmpfile)
    os.unlink(tmpfile)
    return frame

def recognize_face(frame, known_faces, known_names):
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    )
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.05, minNeighbors=5, minSize=(20, 20)
    )
    results = []
    for (x, y, w, h) in faces:
        face_img = gray[y:y+h, x:x+w]
        face_img = cv2.resize(face_img, (150, 150))
        face_img = cv2.equalizeHist(face_img)
        best_score = float('inf')
        best_name = "Unknown"
        for i, person_images in enumerate(known_faces):
            for known_img in person_images:
                known_resized = cv2.resize(known_img, (150, 150))
                known_resized = cv2.equalizeHist(known_resized)
                diff = np.mean(np.abs(face_img.astype(int) - known_resized.astype(int)))
                if diff < best_score:
                    best_score = diff
                    best_name = known_names[i]
        if best_score < 150:
            results.append(best_name)
        else:
            results.append("Unknown")
        print(f"Score: {best_score:.1f} -> {results[-1]}")
    return results if results else ["No face"]

if __name__ == "__main__":
    print("Loading known faces...")
    known_faces, known_names = load_known_faces()
    print(f"Loaded: {known_names}")
    frame = capture_frame()
    if frame is not None:
        names = recognize_face(frame, known_faces, known_names)
        print(f"Recognized: {names}")
    else:
        print("Camera capture failed")
PYEOF

# ---- Step 5: Write main.py ----
echo "Writing main.py..."
cat > /home/pi/robot/main.py << 'PYEOF'
import time
import threading
import os
import tempfile
import pickle
import cv2
import numpy as np
import subprocess
from gtts import gTTS
from face_recognition.recognize import load_known_faces, recognize_face, capture_frame
from voice.listener import listen
from ai.assistant import ask_aria

def speak(text):
    print(f"ARIA says: {text}")
    with tempfile.NamedTemporaryFile(suffix='.mp3', delete=False) as f:
        tmpfile = f.name
    tts = gTTS(text=text, lang='en', slow=False)
    tts.save(tmpfile)
    os.system(f"mpg123 -q {tmpfile}")
    os.unlink(tmpfile)

def train_new_face(name):
    speak(f"Okay {name}! I will take 30 photos. Please look at the camera from different angles.")
    faces_dir = "/home/pi/robot/face_recognition/known_faces"
    os.makedirs(faces_dir, exist_ok=True)
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    )
    images = []
    count = 0
    attempts = 0
    angles = [
        "Look straight at the camera",
        "Tilt your head slightly left",
        "Tilt your head slightly right",
        "Look slightly up",
        "Look slightly down",
        "Move a little closer",
        "Move a little farther",
    ]
    while count < 30 and attempts < 60:
        attempts += 1
        if count % 4 == 0:
            speak(angles[min(count // 4, len(angles) - 1)])
            time.sleep(2)
        frame = capture_frame()
        if frame is None:
            continue
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(gray)
        faces = face_cascade.detectMultiScale(gray, 1.1, 5, minSize=(50, 50))
        if len(faces) > 0:
            x, y, w, h = faces[0]
            face_img = gray[y:y+h, x:x+w]
            face_img = cv2.resize(face_img, (150, 150))
            face_img = cv2.equalizeHist(face_img)
            images.append(face_img)
            count += 1
            print(f"Captured {count}/30")
            if count % 10 == 0:
                speak(f"{count} photos done, keep going!")
            time.sleep(0.5)
        else:
            time.sleep(0.3)
    if count >= 20:
        data = {"name": name, "images": images}
        save_path = os.path.join(faces_dir, f"{name}.pkl")
        with open(save_path, "wb") as f:
            pickle.dump(data, f)
        speak(f"Done! I will now remember you {name}!")
        global known_faces, known_names
        known_faces, known_names = load_known_faces()
    else:
        speak("Sorry I could not capture enough photos. Try again with better lighting.")

known_faces, known_names = load_known_faces()
last_greeted = {}
GREET_COOLDOWN = 30
aria_busy = False

def scan_once():
    global aria_busy
    try:
        frame = capture_frame()
        if frame is None:
            return
        names = recognize_face(frame, known_faces, known_names)
        for name in names:
            if name not in ["No face", "Unknown"]:
                now = time.time()
                if name not in last_greeted or (now - last_greeted[name]) > GREET_COOLDOWN:
                    aria_busy = True
                    speak(f"Hi {name}! Good to see you!")
                    last_greeted[name] = now
                    aria_busy = False
    except Exception as e:
        print(f"Camera error: {e}")

def camera_loop():
    print("Camera started...")
    while True:
        if not aria_busy:
            scan_once()
        time.sleep(5)

def handle_command(command):
    global aria_busy
    if command is None:
        return True
    command = command.lower().strip()
    print(f"Command: {command}")
    if any(w in command for w in ["stop", "bye", "goodbye", "exit", "quit"]):
        speak("Goodbye! See you soon!")
        return False
    if "who are you" in command or "your name" in command:
        speak("I am ARIA, your AI Robot Intelligence Assistant!")
        return True
    if "train me" in command or "remember me" in command or "learn me" in command:
        speak("Sure! What is your name?")
        name = listen()
        if name:
            train_new_face(name.strip().capitalize())
        else:
            speak("Sorry I did not catch your name. Please try again.")
        return True
    if "who am i" in command or "do you know me" in command:
        aria_busy = True
        frame = capture_frame()
        if frame is not None:
            names = recognize_face(frame, known_faces, known_names)
            if names and names[0] not in ["No face", "Unknown"]:
                speak(f"You are {names[0]}! I know you!")
            else:
                speak("I am not sure who you are. Say train me so I can learn your face!")
        aria_busy = False
        return True
    if "weather" in command:
        try:
            from ai.weather import get_weather
            speak(get_weather())
        except Exception:
            speak("Sorry I could not get the weather right now.")
        return True
    try:
        response = ask_aria(command)
        speak(response)
    except Exception as e:
        speak("Sorry I could not get a response right now.")
        print(f"AI error: {e}")
    return True

def run_aria():
    global aria_busy
    speak("Hello! I am ARIA, your AI Robot Intelligence Assistant! I am ready!")
    cam_thread = threading.Thread(target=camera_loop, daemon=True)
    cam_thread.start()
    running = True
    while running:
        if aria_busy:
            time.sleep(0.5)
            continue
        print("\nListening...")
        command = listen()
        running = handle_command(command)
    speak("ARIA shutting down. Goodbye!")

if __name__ == "__main__":
    run_aria()
PYEOF

# ---- Step 6: Create systemd service ----
echo "Creating systemd service..."
sudo tee /etc/systemd/system/aria.service > /dev/null << 'SVCEOF'
[Unit]
Description=ARIA Robot
After=network.target bluetooth.target sound.target

[Service]
ExecStartPre=/bin/sleep 15
ExecStartPre=/usr/bin/rfkill unblock bluetooth
ExecStartPre=/usr/sbin/hciconfig hci0 up
ExecStart=/usr/bin/python3 /home/pi/robot/main.py
WorkingDirectory=/home/pi/robot
User=pi
Restart=on-failure
RestartSec=5

[Install]
WantedBy=multi-user.target
SVCEOF

sudo systemctl daemon-reload
sudo systemctl enable aria.service
echo "Systemd service enabled."

# ---- Step 7: Bluetooth setup ----
echo "Setting up Bluetooth..."
sudo rfkill unblock bluetooth
sudo hciconfig hci0 up
echo -e "power on\nagent on\ndefault-agent\nconnect 41:42:78:94:D0:DD\nquit" | bluetoothctl || true
sleep 3

# ---- Step 8: Test speaker ----
echo "=== TEST: Speaker ==="
python3 /home/pi/robot/voice/speaker.py && echo "SPEAKER_TEST_OK" || echo "SPEAKER_TEST_FAILED"

# ---- Step 9: Test camera ----
echo "=== TEST: Camera ==="
rpicam-jpeg -o /tmp/test_cam.jpg --timeout 1000 -n && echo "CAMERA_TEST_OK" || echo "CAMERA_TEST_FAILED"

echo ""
echo "=== ARIA Setup Complete ==="
echo "To start ARIA manually: cd /home/pi/robot && python3 main.py"
echo "To check service status: sudo systemctl status aria"
echo "ARIA will auto-start on next reboot."

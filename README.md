# ARIA — AI Robot Intelligence Assistant

<p align="center">
  <img src="https://img.shields.io/badge/Platform-Raspberry%20Pi%20Zero%202W-red?style=for-the-badge&logo=raspberrypi" alt="Raspberry Pi"/>
  <img src="https://img.shields.io/badge/Platform-Arduino%20Uno-blue?style=for-the-badge&logo=arduino" alt="Arduino"/>
  <img src="https://img.shields.io/badge/Language-Python%203-yellow?style=for-the-badge&logo=python" alt="Python"/>
  <img src="https://img.shields.io/badge/AI-Claude%20API-green?style=for-the-badge" alt="Claude AI"/>
  <img src="https://img.shields.io/badge/License-MIT-purple?style=for-the-badge" alt="MIT License"/>
</p>

<p align="center">
  <strong>A fully autonomous AI robot that sees you, knows you, listens to you, and follows you.</strong><br/>
  Built by <a href="https://github.com/bala2207022">Balakrishna Reddy Channareddy</a> · MS Business Analytics · University of the Pacific
</p>

---

## What is ARIA?

ARIA (**A**I **R**obot **I**ntelligence **A**ssistant) is an autonomous AI robot built on **Raspberry Pi Zero 2W** and **Arduino Uno**.  
It combines computer vision, voice recognition, AI-powered responses, pan-tilt servo tracking, and autonomous 4WD navigation.

**This is not a remote-controlled toy.** ARIA thinks, listens, and reacts on its own.

---

## Demo

```
You walk into the room…

ARIA: "Hey Bala! Good to see you!"

You: "ARIA, what's the weather today?"

ARIA: "It's 72°F and sunny in Stockton. Perfect day to go outside!"

You start walking away…

ARIA: *pan-tilt servo tracks your face and motors follow you*
```

---

## Features

| Feature | Description |
|---------|-------------|
| **Face Recognition** | Identifies people by face and greets them by name |
| **Voice Commands** | Listens and responds to natural speech |
| **AI Conversations** | Claude API answers questions, tells jokes, holds conversations |
| **Pan-Tilt Tracking** | Dual SG90 servos keep the camera centred on your face |
| **iPhone Following** | HM-10 BLE module detects phone proximity and drives toward you |
| **Obstacle Avoidance** | HC-SR04 ultrasonic sensor detects and steers around objects |
| **Live Weather** | Real-time weather for Stockton, CA via OpenWeatherMap |
| **Bluetooth Audio** | Voice output through BTS001 Bluetooth speaker via gTTS |

---

## How It Works

```
┌──────────────────────────────────────────────────────────────┐
│                        ARIA WORKFLOW                          │
└──────────────────────────────────────────────────────────────┘

   ┌─────────┐     ┌─────────┐     ┌─────────┐     ┌─────────┐
   │  SEES   │ ──► │ THINKS  │ ──► │ SPEAKS  │ ──► │ MOVES   │
   │  (Eyes) │     │ (Brain) │     │ (Voice) │     │ (Wheels)│
   └─────────┘     └─────────┘     └─────────┘     └─────────┘
       │               │               │               │
    Camera         Claude AI       BT Speaker       4WD Motors
    (OV5647)     (Raspberry Pi)     (gTTS)          (L298N)
```

1. **Power On** — ARIA boots, initialises all systems  
2. **Scan** — Camera captures a 320×240 frame every 5 seconds  
3. **Recognise** — Haar-cascade + pixel-diff identifies who you are  
4. **Greet** — *"Hey Bala! Good to see you!"*  
5. **Listen** — Microphone waits for a voice command  
6. **Process** — Google Speech Recognition converts audio to text  
7. **Think** — Claude API generates a short spoken response  
8. **Respond** — gTTS plays the answer through the Bluetooth speaker  
9. **Track** — Pan servo (GPIO 18) keeps the camera on your face  
10. **Follow** — Arduino drives the motors toward you  

---

## System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    ARIA SYSTEM OVERVIEW                      │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌──────────────────────┐    ┌──────────────────────┐       │
│  │   RASPBERRY PI       │    │      ARDUINO         │       │
│  │   (The Brain)        │    │    (The Muscles)     │       │
│  │                      │    │                      │       │
│  │  • Face Recognition  │    │  • Motor Control     │       │
│  │  • Voice Processing  │◄──►│  • Obstacle Sensing  │       │
│  │  • AI Responses      │    │  • BLE Phone Follow  │       │
│  │  • Pan-Tilt Servos   │    │                      │       │
│  └──────────────────────┘    └──────────────────────┘       │
│           │                           │                      │
│           ▼                           ▼                      │
│  ┌──────────────────────────────────────────────────┐       │
│  │              SENSORS & PERIPHERALS                │       │
│  │                                                   │       │
│  │  OV5647 Camera   SuziePi USB Mic   BT Speaker    │       │
│  │  SG90 Pan Servo  SG90 Tilt Servo  HC-SR04        │       │
│  │  HM-10 BLE       L298N Motor Driver  Power Bank  │       │
│  └──────────────────────────────────────────────────┘       │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## Hardware

| Component | Model | Purpose |
|-----------|-------|---------|
| Single Board Computer | Raspberry Pi Zero 2W (512 MB) | Main AI brain |
| Microcontroller | LAFVIN Arduino Uno R3 | Motor & sensor control |
| Camera | OV5647 5 MP Night Vision | Face detection & tracking |
| Microphone | SuziePi USB Mini Mic | Voice input |
| Speaker | BTS001 Bluetooth Speaker | Audio output |
| Pan Servo | SG90 Servo Motor | Left/right camera tracking |
| Tilt Servo | SG90 Servo Motor | Up/down camera tracking |
| Motor Driver | L298N H-Bridge | Motor control |
| Ultrasonic | HC-SR04 | Obstacle detection |
| BLE Module | HM-10 Bluetooth 4.0 | iPhone following |
| Chassis | 4WD Robot Car Kit | Mobility platform |
| Power | Power Bank + USB Wall Charger | Pi & Arduino power |

---

## Wiring

### Raspberry Pi GPIO

| Component | Pi Pin | GPIO | Wire |
|-----------|--------|------|------|
| Pan Servo Signal | Pin 12 | GPIO 18 | Orange |
| Tilt Servo Signal | Pin 16 | GPIO 23 | Orange |
| Both Servos VCC | Pin 2 | 5 V | Red |
| Both Servos GND | Pin 6 | GND | Brown/Black |

### Arduino Uno

| Component | Arduino Pin | Notes |
|-----------|-------------|-------|
| L298N ENA | Pin 5 (PWM) | Left motor speed |
| L298N ENB | Pin 9 (PWM) | Right motor speed |
| L298N IN1 | Pin 3 | Left motor direction A |
| L298N IN2 | Pin 4 | Left motor direction B |
| L298N IN3 | Pin 7 | Right motor direction A |
| L298N IN4 | Pin 8 | Right motor direction B |
| HC-SR04 TRIG | Pin 10 | Ultrasonic trigger |
| HC-SR04 ECHO | Pin 11 | Ultrasonic echo |
| HM-10 TX | Pin 2 | BLE receive |
| HM-10 RX | Pin 12 | BLE transmit |
| HM-10 VCC | 3.3 V | **Must be 3.3 V, not 5 V!** |
| HM-10 GND | GND | Ground |

### L298N Motor Driver

| Terminal | Connects To |
|----------|-------------|
| OUT1, OUT2 | Left side motors (both) |
| OUT3, OUT4 | Right side motors (both) |
| 12 V (VMS) | Battery pack positive |
| GND | Battery pack negative + Arduino GND |

> **Important:** Power the Arduino via a USB wall charger separately.  
> Power the Pi via a power bank.

---

## Software Stack

| Technology | Purpose |
|------------|---------|
| Python 3 | Main programming language |
| OpenCV | Real-time computer vision (Haar cascades) |
| Google Speech API | Speech-to-text conversion |
| gTTS + mpg123 | Text-to-speech output |
| Claude API (`claude-sonnet-4-20250514`) | AI response generation |
| OpenWeatherMap API | Live weather data |
| Arduino C++ | Motor and sensor control |
| SoftwareSerial | HM-10 BLE communication |

---

## Project Structure

```
ARIA/
│
├── README.md                        # You are here
├── requirements.txt                 # Python dependencies
├── .env.example                     # API key template
├── main.py                          # Main entry point — starts ARIA
│
├── ai/
│   ├── assistant.py                 # Claude API integration
│   └── weather.py                   # OpenWeatherMap integration
│
├── voice/
│   ├── listener.py                  # Captures voice commands
│   └── speaker.py                   # Speaks responses via gTTS
│
├── face_recognition/
│   ├── recognize.py                 # Real-time face recognition
│   ├── train.py                     # Train ARIA to recognise a face
│   └── known_faces/                 # Saved face data (.pkl)
│
└── motor_control/
    ├── servo.py                     # Pan-tilt servo utility class
    └── aria_motors.ino              # Arduino motor & BLE sketch
```

---

## Installation

### Prerequisites

- Raspberry Pi Zero 2W with Raspberry Pi OS Legacy (32-bit) installed  
- Arduino Uno connected via USB  
- All hardware wired as above

### Step 1 — Clone the Repository

```bash
git clone https://github.com/bala2207022/ARIA_robot.git ~/robot
cd ~/robot
```

### Step 2 — Install System Packages

```bash
sudo apt-get update
sudo apt-get install -y espeak flac mpg123 python3-pyaudio python3-opencv libopencv-dev
```

### Step 3 — Install Python Packages

```bash
pip3 install anthropic speechrecognition gtts python-dotenv requests RPi.GPIO --break-system-packages
```

### Step 4 — Configure API Keys

```bash
cp .env.example .env
# Edit .env and fill in your keys
```

```env
CLAUDE_API_KEY=your_claude_api_key_here
WEATHER_API_KEY=your_openweathermap_key
NEWS_API_KEY=your_newsapi_key
```

### Step 5 — Connect Bluetooth Speaker

```bash
sudo rfkill unblock bluetooth
sudo hciconfig hci0 up
bluetoothctl
# Inside bluetoothctl:
power on
agent on
scan on
# When BTS001 appears:
pair   41:42:78:94:D0:DD
trust  41:42:78:94:D0:DD
connect 41:42:78:94:D0:DD
exit
```

### Step 6 — Train Face Recognition

```bash
python3 ~/robot/face_recognition/train.py
# Enter your name when prompted
# Stand 3–4 feet from the camera
# Move head slowly in different directions
```

### Step 7 — Upload Arduino Sketch

1. Open `motor_control/aria_motors.ino` in Arduino IDE  
2. **Disconnect HM-10 TX/RX wires** before uploading  
3. Select **Board: Arduino UNO** and the correct **Port**  
4. Click **Upload**, then reconnect HM-10 wires

### Step 8 — Run ARIA

```bash
# Connect Bluetooth speaker first
bluetoothctl
connect 41:42:78:94:D0:DD
exit

cd ~/robot && python3 main.py
```

---

## Voice Commands

| Say This | ARIA Does This |
|----------|----------------|
| *"Hello ARIA"* | ARIA greets you |
| *"Who are you"* | ARIA introduces itself |
| *"Who am I"* | ARIA scans and identifies your face |
| *"Remember me" / "Train me"* | ARIA learns your face (20 photos) |
| *"What's the weather"* | Live weather for Stockton, CA |
| *"What time is it"* | Current time |
| *Any question* | Claude AI answers intelligently |
| *"Goodbye" / "Bye"* | ARIA shuts down cleanly |

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| SSH not connecting | Turn hotspot off/on. Run: `ssh-keygen -R aria.local` |
| Bluetooth not connecting | `sudo rfkill unblock bluetooth && sudo hciconfig hci0 up` |
| Speaker no sound | Reconnect: `bluetoothctl → connect 41:42:78:94:D0:DD` |
| Camera not detecting face | Stand 3–4 feet away, good lighting, face camera directly |
| Servo not moving | Check GPIO 18/23 wiring |
| Mic not responding | Speak loudly and clearly; check device index in `listener.py` |
| AI not responding | Check `.env` has a valid `CLAUDE_API_KEY` |
| Motors not moving | Check L298N wiring and battery connection |
| Arduino upload fails | Disconnect HM-10 TX/RX wires before uploading |
| `cv2.data` path error | Use `/usr/share/opencv4/haarcascades/` directly |

---

## Future Improvements

- RSSI-based automatic phone following via HC-05 / HM-10  
- Wide-angle camera lens for a better field of view  
- Offline voice recognition using Vosk  
- GPS-based outdoor navigation  
- Mobile app for remote ARIA control  
- Multi-person simultaneous face recognition  
- Emotion detection from facial expressions  
- Spotify music control integration  
- Home automation integration  

---

## License

MIT License — see [LICENSE](LICENSE) for details.

---

<p align="center">
  ARIA Project · Balakrishna Reddy Channareddy · <a href="https://github.com/bala2207022/ARIA_robot">github.com/bala2207022/ARIA_robot</a>
</p>


<p align="center">
  <img src="https://img.shields.io/badge/Platform-Raspberry%20Pi-red?style=for-the-badge&logo=raspberrypi" alt="Raspberry Pi"/>
  <img src="https://img.shields.io/badge/Platform-Arduino-blue?style=for-the-badge&logo=arduino" alt="Arduino"/>
  <img src="https://img.shields.io/badge/Language-Python-yellow?style=for-the-badge&logo=python" alt="Python"/>
  <img src="https://img.shields.io/badge/AI-Claude%20API-green?style=for-the-badge" alt="AI"/>
  <img src="https://img.shields.io/badge/License-MIT-purple?style=for-the-badge" alt="MIT License"/>
</p>

<p align="center">
  <strong>A personal AI robot that sees you, knows you, listens to you, and follows you.</strong>
</p>

---

## What is ARIA?

ARIA is a **fully autonomous AI assistant robot** that combines:

- **Computer Vision** — Recognizes faces and tracks movement
- **Natural Language Processing** — Understands what you say
- **Artificial Intelligence** — Thinks and responds intelligently
- **Mobile Robotics** — Physically follows you around

**This is not a remote-controlled toy.** ARIA thinks, listens, and reacts on its own.

---

## Demo

```
You walk into the room...

ARIA: "Hey Bala! Good to see you!"

You: "ARIA, what's the weather today?"

ARIA: "It's 72°F and sunny in Stockton. Perfect day to go outside!"

You start walking away...

ARIA: *follows you across the room* 🤖
```

---

## Features

| Feature | Description |
|---------|-------------|
| **Face Recognition** | Identifies people by face and greets them by name |
| **Voice Commands** | Listens and responds to natural speech |
| **AI Conversations** | Answers questions, tells jokes, holds conversations |
| **Autonomous Movement** | Follows you around the room automatically |
| **Obstacle Avoidance** | Detects and avoids objects in its path |
| **Bluetooth Tracking** | Finds you in any room using your phone's Bluetooth |
| **Object Detection** | Point camera at anything — ARIA explains it |
| **Live Weather** | Real-time weather updates for your location |

---

## How It Works

```
┌──────────────────────────────────────────────────────────────┐
│                        ARIA WORKFLOW                          │
└──────────────────────────────────────────────────────────────┘

   ┌─────────┐     ┌─────────┐     ┌─────────┐     ┌─────────┐
   │  SEES   │ ──► │ THINKS  │ ──► │ SPEAKS  │ ──► │ MOVES   │
   │  (Eyes) │     │ (Brain) │     │ (Voice) │     │ (Wheels)│
   └─────────┘     └─────────┘     └─────────┘     └─────────┘
       │               │               │               │
    Camera         AI Model        Speaker         Motors
```

### Step-by-Step Flow

1. **Power On** — ARIA boots up and initializes all systems
2. **Scan** — Camera activates and looks for faces
3. **Recognize** — ML model identifies who you are
4. **Greet** — *"Hey Bala! Welcome back!"*
5. **Listen** — Microphone waits for your voice command
6. **Process** — Speech converted to text
7. **Think** — AI generates an intelligent response
8. **Respond** — Answer spoken through speaker
9. **Track** — Camera tracks your position
10. **Follow** — Motors move ARIA toward you

---

## System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    ARIA SYSTEM OVERVIEW                      │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌──────────────────────┐    ┌──────────────────────┐       │
│  │   RASPBERRY PI       │    │      ARDUINO         │       │
│  │   (The Brain)        │    │    (The Muscles)     │       │
│  │                      │    │                      │       │
│  │  • Face Recognition  │    │  • Motor Control     │       │
│  │  • Voice Processing  │◄──►│  • Obstacle Sensing  │       │
│  │  • AI Responses      │    │  • Movement Logic    │       │
│  │  • Decision Making   │    │                      │       │
│  └──────────────────────┘    └──────────────────────┘       │
│           │                           │                      │
│           ▼                           ▼                      │
│  ┌──────────────────────────────────────────────────┐       │
│  │              SENSORS & PERIPHERALS                │       │
│  │                                                   │       │
│  │  📷 Camera     🎤 Microphone    🔊 Speaker       │       │
│  │  📡 Ultrasonic Sensor          🔋 Power Supply   │       │
│  └──────────────────────────────────────────────────┘       │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## Hardware Required

| Component | Model | Purpose |
|-----------|-------|---------|
| Single Board Computer | Raspberry Pi Zero 2W | Main processor — runs ML and AI |
| Microcontroller | Arduino Uno R3 | Motor controller and sensors |
| Camera | Arducam Pi Zero Camera (5MP) | Face detection and tracking |
| Microphone | USB Mini Microphone | Voice input |
| Speaker | Mini Speaker | Voice output |
| Chassis | 4WD Robot Car Kit | Mobility platform |
| Distance Sensor | HC-SR04 Ultrasonic | Obstacle detection |
| Storage | MicroSD Card (32GB) | Operating system and code |

---

## Software Stack

| Technology | Purpose |
|------------|---------|
| **Python 3** | Main programming language |
| **OpenCV** | Real-time computer vision |
| **face_recognition** | ML-based face identification |
| **Google Speech API** | Speech-to-text conversion |
| **pyttsx3 / gTTS** | Text-to-speech output |
| **Claude API** | AI response generation |
| **OpenWeatherMap API** | Live weather data |
| **Arduino IDE (C++)** | Motor and sensor control |
| **PySerial** | Pi ↔ Arduino communication |
| **PyBluez** | Bluetooth tracking |
| **Arduino IDE (C++)** | Motor and sensor control |
| **PySerial** | Pi ↔ Arduino communication |

---

## Project Structure

```
ARIA/
│
├── README.md                    # You are here
├── requirements.txt             # Python dependencies
├── .env.example                 # API key template
│
├── main.py                      # Main entry point — starts ARIA
│
├── ai/                          # Intelligence module
│   └── assistant.py             # Claude API integration
│
├── voice/                       # Audio module
│   ├── listener.py              # Captures voice commands
│   └── speaker.py               # Speaks responses via gTTS
│
├── face_recognition/            # Vision module
│   ├── train.py                 # Train ARIA to recognize faces
│   ├── recognize.py             # Real-time face recognition
│   └── known_faces/             # Stored face encodings
│
└── motor_control/               # Movement module
    └── serial_comm.py           # Sends commands to Arduino
```

---

## Installation

### Prerequisites

- Raspberry Pi Zero 2W with Raspberry Pi OS installed
- Arduino Uno with USB cable
- All hardware components connected

### Step 1: Clone the Repository

```bash
git clone https://github.com/bala2207022/ARIA_robot.git
cd ARIA_robot
```

### Step 2: Install Dependencies

```bash
pip3 install -r requirements.txt
```

### Step 3: Configure API Keys

```bash
cp .env.example .env
# Edit .env and add your API keys
```

### Step 4: Train Face Recognition

```bash
cd pi/face_recognition

# Train ARIA to recognize your face
python3 train.py --name "YourName"

# Follow the prompts — take 15-20 photos from different angles
```

### Step 4: Upload Arduino Code

1. Open `motor_control/aria_motors.ino` in Arduino IDE
2. Select **Board: Arduino Uno**
3. Select the correct **Port**
4. Click **Upload**

### Step 5: Run ARIA

```bash
python3 main.py
```

---

## Environment Variables

Create a `.env` file based on `.env.example`:

```
CLAUDE_API_KEY=your_claude_api_key
WEATHER_API_KEY=your_openweathermap_key
NEWS_API_KEY=your_newsapi_key
```

---

## Voice Commands

| Say This | ARIA Does This |
|----------|----------------|
| *"ARIA, follow me"* | Starts following you |
| *"ARIA, stop"* | Stops all movement |
| *"ARIA, come here"* | Bluetooth tracking to find you |
| *"ARIA, what time is it?"* | Tells current time |
| *"ARIA, what's the weather?"* | Live weather update |
| *"ARIA, tell me a joke"* | Tells a random joke |
| *"ARIA, what is this?"* | Object detection via camera |
| *"ARIA, go to sleep"* | Enters low-power mode |
| *"ARIA, wake up"* | Exits sleep mode |
| *Any question* | AI answers intelligently |

---

## Wiring Diagram

### Raspberry Pi Connections

| Pi Pin | Connects To |
|--------|-------------|
| USB | Arduino (serial communication) |
| USB | USB Microphone |
| Camera Port | Arducam Pi Zero Camera |
| GPIO | Speaker via amplifier |
| 5V / GND | Power supply |
| GND | Common ground |

### Arduino Connections

| Arduino Pin | Connects To |
|-------------|-------------|
| D2 | Ultrasonic TRIG |
| D3 | Ultrasonic ECHO |
| D4-D7 | Motor Driver IN1-IN4 |
| 5V | Motor Driver VCC |
| GND | Common ground |
| USB | Raspberry Pi |

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Camera not detected | Run `sudo raspi-config` and enable camera |
| Face not recognized | Retrain with better lighting and more photos |
| No audio output | Check speaker connection |
| Motors not moving | Verify Arduino wiring and serial connection |
| "No module" error | Run `pip3 install -r requirements.txt` |
| ARIA not responding | Check microphone and verify API keys in `.env` |

---

## Future Enhancements

- [ ] Emotion detection from facial expressions
- [ ] Gesture recognition for hand commands
- [ ] Home automation integration (smart lights, etc.)
- [ ] Mobile app for remote monitoring
- [ ] Multi-person tracking
- [ ] SLAM for room mapping
- [ ] Spotify music control
- [ ] Google Calendar integration

---

## Author

**Bala**  
MS Business Analytics — University of the Pacific  
Teaching Assistant — Python for AI Models

---

## License

This project is open source under the [MIT License](LICENSE).

---

<p align="center">
  <em>Built with curiosity, Python, and way too many jumper wires. 🔌</em>
</p>

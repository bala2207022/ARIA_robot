# ARIA — AI Robot Intelligence Assistant

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

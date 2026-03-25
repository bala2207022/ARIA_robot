# ARIA — AI Robot Intelligence Assistant

<p align="center">
  <img src="https://img.shields.io/badge/Platform-Raspberry%20Pi-red?style=for-the-badge&logo=raspberrypi" alt="Raspberry Pi"/>
  <img src="https://img.shields.io/badge/Platform-Arduino-blue?style=for-the-badge&logo=arduino" alt="Arduino"/>
  <img src="https://img.shields.io/badge/Language-Python-yellow?style=for-the-badge&logo=python" alt="Python"/>
  <img src="https://img.shields.io/badge/AI-Powered-green?style=for-the-badge&logo=openai" alt="AI"/>
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

| Component | Model | Purpose | Approx. Cost |
|-----------|-------|---------|--------------|
| Single Board Computer | Raspberry Pi Zero 2W | Main processor — runs ML and AI | $15 |
| Microcontroller | Arduino Uno R3 | Motor controller and sensors | $25 |
| Camera | Pi Camera Module (5MP) | Face detection and tracking | $25 |
| Microphone | USB Mini Microphone | Voice input | $8 |
| Speaker | Mini 3W Speaker | Voice output | $5 |
| Chassis | 4WD Robot Car Kit | Mobility platform | $30 |
| Distance Sensor | HC-SR04 Ultrasonic | Obstacle detection | $3 |
| Power | 18650 Battery Pack | Power supply | $15 |
| Misc | Jumper wires, breadboard | Connections | $10 |

**Estimated Total: ~$136**

---

## Software Stack

| Technology | Purpose |
|------------|---------|
| **Python 3** | Main programming language |
| **OpenCV** | Real-time computer vision |
| **face_recognition** | ML-based face identification |
| **Google Speech API** | Speech-to-text conversion |
| **pyttsx3 / gTTS** | Text-to-speech output |
| **OpenAI / Claude API** | AI response generation |
| **Arduino IDE (C++)** | Motor and sensor control |
| **PySerial** | Pi ↔ Arduino communication |

---

## Project Structure

```
ARIA/
│
├── README.md                    # You are here
│
├── pi/                          # Raspberry Pi code
│   │
│   ├── main.py                  # Main entry point — starts ARIA
│   │
│   ├── face_recognition/        # Vision module
│   │   ├── train.py             # Train ARIA to recognize faces
│   │   ├── recognize.py         # Real-time face recognition
│   │   └── known_faces/         # Stored face data
│   │       └── bala.pkl         # Example: Bala's face encoding
│   │
│   ├── voice/                   # Audio module
│   │   ├── listener.py          # Captures voice commands
│   │   └── speaker.py           # Speaks responses
│   │
│   ├── ai/                      # Intelligence module
│   │   └── assistant.py         # Handles AI conversations
│   │
│   └── motor_control/           # Movement module
│       └── serial_comm.py       # Sends commands to Arduino
│
└── arduino/                     # Arduino code
    └── aria_motors/
        └── aria_motors.ino      # Motor + ultrasonic sensor logic
```

---

## Installation

### Prerequisites

- Raspberry Pi with Raspberry Pi OS installed
- Arduino Uno with USB cable
- All hardware components connected

### Step 1: Set Up Raspberry Pi

```bash
# Update system
sudo apt-get update && sudo apt-get upgrade -y

# Install system dependencies
sudo apt-get install -y python3-pip python3-opencv libatlas-base-dev

# Install Python packages
pip3 install face_recognition SpeechRecognition pyttsx3 pyserial openai
```

### Step 2: Enable Camera

```bash
sudo raspi-config
# Navigate to: Interface Options → Camera → Enable
# Reboot when prompted
```

### Step 3: Train Face Recognition

```bash
cd pi/face_recognition

# Train ARIA to recognize your face
python3 train.py --name "YourName"

# Follow the prompts — take 15-20 photos from different angles
```

### Step 4: Upload Arduino Code

1. Open `arduino/aria_motors/aria_motors.ino` in Arduino IDE
2. Select **Board: Arduino Uno**
3. Select the correct **Port**
4. Click **Upload**

### Step 5: Configure AI API

```bash
# Set your API key (OpenAI or Claude)
export OPENAI_API_KEY="your-api-key-here"

# Or add to ~/.bashrc for persistence
echo 'export OPENAI_API_KEY="your-key"' >> ~/.bashrc
```

### Step 6: Run ARIA

```bash
cd pi
python3 main.py
```

ARIA is now active!

---

## Voice Commands

| Say This | ARIA Does This |
|----------|----------------|
| *"ARIA, follow me"* | Starts following you |
| *"ARIA, stop"* | Stops all movement |
| *"ARIA, who am I?"* | Tells you who it recognizes |
| *"ARIA, what time is it?"* | Tells current time |
| *"ARIA, tell me a joke"* | Tells a random joke |
| *"ARIA, what's the weather?"* | Gives weather update |
| *"ARIA, go to sleep"* | Enters low-power mode |
| *"ARIA, wake up"* | Exits sleep mode |
| *"ARIA, how are you?"* | Responds conversationally |
| *Any question* | AI answers intelligently |

---

## Wiring Diagram

### Raspberry Pi Connections

| Pi Pin | Connects To |
|--------|-------------|
| USB | Arduino (for serial communication) |
| USB | USB Microphone |
| Camera Port | Pi Camera Module |
| 3.5mm Audio / GPIO | Speaker |
| 5V | Power (via battery pack) |
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
| No audio output | Check speaker connection, run `speaker-test` |
| Motors not moving | Verify Arduino wiring and serial connection |
| "No module" error | Install missing package with `pip3 install <package>` |
| ARIA not responding | Check microphone connection, verify API key |

---

## Future Enhancements

- [ ] Add emotion detection from facial expressions
- [ ] Implement gesture recognition for hand commands
- [ ] Add home automation integration (smart lights, etc.)
- [ ] Build mobile app for remote monitoring
- [ ] Add multi-person tracking
- [ ] Implement SLAM for room mapping

---

## Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

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
  <em>Built with curiosity, Python, and way too many jumper wires.</em>
</p>

#include <SoftwareSerial.h>

// Motor driver (L298N)
#define ENA 5   // PWM – left motor speed
#define ENB 9   // PWM – right motor speed
#define IN1 3   // Left motor direction A
#define IN2 4   // Left motor direction B
#define IN3 7   // Right motor direction A
#define IN4 8   // Right motor direction B

// Ultrasonic sensor (HC-SR04)
#define TRIG 10
#define ECHO 11

// HM-10 BLE module via SoftwareSerial (RX=pin2, TX=pin12)
SoftwareSerial BTSerial(2, 12);

String input      = "";
bool   phoneNear  = false;
String lastAction = "";

// ── Motor helpers ────────────────────────────────────────────────────────────

void stopMotors() {
  if (lastAction == "STOP") return;
  analogWrite(ENA, 0);  analogWrite(ENB, 0);
  digitalWrite(IN1, LOW); digitalWrite(IN2, LOW);
  digitalWrite(IN3, LOW); digitalWrite(IN4, LOW);
  lastAction = "STOP";
}

void forward() {
  if (lastAction == "FORWARD") return;
  analogWrite(ENA, 200); analogWrite(ENB, 200);
  digitalWrite(IN1, HIGH); digitalWrite(IN2, LOW);
  digitalWrite(IN3, HIGH); digitalWrite(IN4, LOW);
  lastAction = "FORWARD";
}

void backward() {
  analogWrite(ENA, 200); analogWrite(ENB, 200);
  digitalWrite(IN1, LOW);  digitalWrite(IN2, HIGH);
  digitalWrite(IN3, LOW);  digitalWrite(IN4, HIGH);
  lastAction = "BACKWARD";
}

void turnRight() {
  analogWrite(ENA, 180); analogWrite(ENB, 180);
  digitalWrite(IN1, HIGH); digitalWrite(IN2, LOW);
  digitalWrite(IN3, LOW);  digitalWrite(IN4, HIGH);
  lastAction = "RIGHT";
}

void turnLeft() {
  analogWrite(ENA, 180); analogWrite(ENB, 180);
  digitalWrite(IN1, LOW);  digitalWrite(IN2, HIGH);
  digitalWrite(IN3, HIGH); digitalWrite(IN4, LOW);
  lastAction = "LEFT";
}

// ── Ultrasonic distance (cm) ─────────────────────────────────────────────────

long getDistance() {
  digitalWrite(TRIG, LOW);  delayMicroseconds(2);
  digitalWrite(TRIG, HIGH); delayMicroseconds(10);
  digitalWrite(TRIG, LOW);
  long duration = pulseIn(ECHO, HIGH, 30000);
  if (duration == 0) return 999;
  return duration * 0.034 / 2;
}

// ── Setup ────────────────────────────────────────────────────────────────────

void setup() {
  Serial.begin(9600);
  BTSerial.begin(9600);

  pinMode(ENA, OUTPUT); pinMode(ENB, OUTPUT);
  pinMode(IN1, OUTPUT); pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT); pinMode(IN4, OUTPUT);
  pinMode(TRIG, OUTPUT); pinMode(ECHO, INPUT);

  stopMotors();
  Serial.println("ARIA Ready!");
}

// ── Main loop ─────────────────────────────────────────────────────────────────

void loop() {
  // Read BLE commands
  while (BTSerial.available()) {
    char c = BTSerial.read();
    if (c == '\n' || c == '\r') continue;
    input += c;
    delay(10);
  }

  if (input.length() > 0) {
    input.trim();
    input.toLowerCase();

    if      (input == "near") phoneNear = true;
    else if (input == "far")  phoneNear = false;
    else if (input == "f")  { lastAction = ""; forward();   }
    else if (input == "b")  { lastAction = ""; backward();  }
    else if (input == "l")  { lastAction = ""; turnLeft();  }
    else if (input == "r")  { lastAction = ""; turnRight(); }
    else if (input == "s")  { lastAction = ""; stopMotors(); }

    input = "";
  }

  long distance = getDistance();

  if (phoneNear) {
    // Phone is close — stay put
    stopMotors();
  } else {
    if (distance < 20 && distance > 0) {
      // Obstacle: back up and steer around it
      stopMotors(); delay(300);
      backward();   delay(400);
      stopMotors(); delay(200);

      long dL, dR;
      turnLeft();  delay(300); stopMotors();
      dL = getDistance();
      turnRight(); delay(600); stopMotors();
      dR = getDistance();

      if (dL > dR) { turnLeft(); delay(300); }
      else         { turnRight(); delay(300); }
      stopMotors(); delay(200);
      lastAction = "";
    } else {
      forward();
    }
  }

  delay(100);
}

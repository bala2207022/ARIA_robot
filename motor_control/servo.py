import RPi.GPIO as GPIO
import time


class ServoController:
    FRAME_WIDTH = 640
    DEAD_ZONE_PX = 30
    GAIN = 0.06
    MIN_ANGLE_STEP = 2

    def __init__(self, pin=18, initial_angle=90):
        self.pin = pin
        self.current_angle = initial_angle
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.OUT)
        try:
            # Clean up any leftover PWM from a previous run
            GPIO.cleanup(pin)
            GPIO.setup(pin, GPIO.OUT)
        except Exception:
            pass
        self.pwm = GPIO.PWM(pin, 50)
        self.pwm.start(0)
        self._apply_angle(initial_angle)

    def _apply_angle(self, angle):
        duty = 2.5 + (angle / 180.0) * 10
        self.pwm.ChangeDutyCycle(duty)
        time.sleep(0.3)
        self.pwm.ChangeDutyCycle(0)

    def set_angle(self, angle):
        angle = max(0, min(180, angle))
        if abs(angle - self.current_angle) < self.MIN_ANGLE_STEP:
            return
        self._apply_angle(angle)
        self.current_angle = angle
        print(f"Servo -> {self.current_angle} deg")

    def track_face(self, face_x):
        offset = face_x - (self.FRAME_WIDTH // 2)
        if abs(offset) < self.DEAD_ZONE_PX:
            return
        new_angle = self.current_angle - (offset * self.GAIN)
        self.set_angle(round(new_angle))

    def center(self):
        self.set_angle(90)

    def cleanup(self):
        self.pwm.stop()
        GPIO.cleanup()

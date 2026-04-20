import cv2
import pickle
import os
import subprocess
import tempfile
import time

HAARCASCADE  = '/usr/share/opencv4/haarcascades/haarcascade_frontalface_default.xml'
FACES_DIR    = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'known_faces')

PROMPTS = [
    'Look straight',
    'Tilt left',
    'Tilt right',
    'Look up',
    'Look down',
]


def _capture_frame():
    with tempfile.NamedTemporaryFile(suffix='.jpg', delete=False) as f:
        tmp = f.name
    subprocess.run(
        ['rpicam-jpeg', '-o', tmp, '--timeout', '500',
         '-n', '--width', '320', '--height', '240'],
        capture_output=True,
    )
    frame = cv2.imread(tmp)
    try:
        os.unlink(tmp)
    except OSError:
        pass
    return frame


def train_face(name: str, speak_fn=None) -> bool:
    """Capture ~20 face images and save them to known_faces/<name>.pkl."""
    os.makedirs(FACES_DIR, exist_ok=True)

    save_path = os.path.join(FACES_DIR, f'{name}.pkl')
    if os.path.exists(save_path):
        if speak_fn:
            speak_fn(f'I already know you, {name}!')
        return True

    face_cascade = cv2.CascadeClassifier(HAARCASCADE)
    images, count, attempts = [], 0, 0

    if speak_fn:
        speak_fn(f'Okay {name}! I will take 20 photos.')

    while count < 20 and attempts < 100:
        attempts += 1

        # Give a prompt every 4 captures
        if count % 4 == 0 and count // 4 < len(PROMPTS):
            if speak_fn:
                speak_fn(PROMPTS[count // 4])
            time.sleep(1)

        frame = _capture_frame()
        if frame is None:
            time.sleep(0.3)
            continue

        gray  = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray  = cv2.equalizeHist(gray)
        faces = face_cascade.detectMultiScale(gray, 1.05, 3, minSize=(30, 30))

        if len(faces) > 0:
            x, y, w, h = faces[0]
            face_img = cv2.resize(cv2.equalizeHist(gray[y:y+h, x:x+w]), (150, 150))
            images.append(face_img)
            count += 1
            print(f'Captured {count}/20')
            time.sleep(0.4)
        else:
            time.sleep(0.3)

    if count >= 15:
        with open(save_path, 'wb') as f:
            pickle.dump({'name': name, 'images': images}, f)
        if speak_fn:
            speak_fn(f'Done! I will remember you, {name}!')
        return True

    if speak_fn:
        speak_fn('Sorry, I could not capture enough photos. Try again with better lighting.')
    return False


if __name__ == '__main__':
    train_face('Bala', speak_fn=print)
import cv2
import pickle
import os
import numpy as np
import subprocess
import tempfile

# Use the system OpenCV haarcascades path (Raspberry Pi OS)
HAARCASCADE = '/usr/share/opencv4/haarcascades/haarcascade_frontalface_default.xml'
FACES_DIR   = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'known_faces')


def load_known_faces():
    known_faces, known_names = [], []
    os.makedirs(FACES_DIR, exist_ok=True)
    for file in os.listdir(FACES_DIR):
        if file.endswith('.pkl'):
            with open(os.path.join(FACES_DIR, file), 'rb') as f:
                data = pickle.load(f)
                known_names.append(data['name'])
                known_faces.append(data['images'])
    return known_faces, known_names


def capture_frame():
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


def recognize_face(frame, known_faces, known_names):
    """
    Returns (names, positions) where positions are (cx, cy) centre tuples.
    """
    face_cascade = cv2.CascadeClassifier(HAARCASCADE)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)

    faces = face_cascade.detectMultiScale(gray, 1.05, 3, minSize=(30, 30))
    if len(faces) == 0:
        faces = face_cascade.detectMultiScale(gray, 1.01, 1, minSize=(20, 20))

    results, positions = [], []
    for (x, y, w, h) in faces:
        cx, cy = int(x + w // 2), int(y + h // 2)
        positions.append((cx, cy))
        face_img = cv2.resize(cv2.equalizeHist(gray[y:y+h, x:x+w]), (150, 150))

        best_score, best_name = float('inf'), 'Unknown'
        for i, person_images in enumerate(known_faces):
            for ki in person_images:
                diff = np.mean(
                    np.abs(face_img.astype(int) - cv2.resize(ki, (150, 150)).astype(int))
                )
                if diff < best_score:
                    best_score, best_name = diff, known_names[i]

        label = best_name if best_score < 150 else 'Unknown'
        results.append(label)
        print(f'Score: {best_score:.1f} -> {label}')

    return (results, positions) if results else (['No face'], [])


if __name__ == '__main__':
    print('Loading known faces…')
    kf, kn = load_known_faces()
    print(f'Loaded: {kn}')
    frame = capture_frame()
    if frame is not None:
        names, positions = recognize_face(frame, kf, kn)
        print(f'Recognized: {names}')
        print(f'Positions:  {positions}')
    else:
        print('Camera capture failed')
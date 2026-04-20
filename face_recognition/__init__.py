# ARIA Face Recognition Module
from .recognize import load_known_faces, recognize_face
from .train import train_face

__all__ = ['load_known_faces', 'recognize_face', 'train_face']

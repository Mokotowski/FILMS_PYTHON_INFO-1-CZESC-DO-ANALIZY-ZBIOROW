import os
import cv2

folder = 'F:\\Filmy gotowe'
file_info = []

valid_extensions = ['.3g2', '.avi', '.mkv', '.mp4', '.mts', '.ts']

for f in os.scandir(folder):
    if f.is_file() and f.name.endswith(tuple(valid_extensions)):
        video = cv2.VideoCapture(f.path)
        width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = int(video.get(cv2.CAP_PROP_FPS))
        file_info.append((f.name, f.stat().st_size, width, height, fps, f.path))
        video.release()

with open('F:\\resolution.txt', 'w') as file:
    for name, size, width, height, fps, path in file_info:
        file.write(f"'{fps}','{height}','{width}\n")

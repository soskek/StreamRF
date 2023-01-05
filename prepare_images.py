from pathlib import Path
import tqdm
import cv2
import os

def video_to_images(video_dir):
    os.makedirs(video_dir / "images", exist_ok=True)
    for video_path in tqdm.tqdm(sorted(Path(video_dir).glob("*.mp4"))):
        print(video_path)
        cap = cv2.VideoCapture(str(video_path))
        if not cap.isOpened():
            print("failed to load {video_path}")
            continue
        while True:
            ret, frame = cap.read()
            name = video_path.stem.split("cam_")[1].zfill(2) + ".png"
            cv2.imwrite(str(video_dir / "images" / name), frame)
            break
        del cap

if __name__ == "__main__":
    video_dir = Path("dataset/MeetRoom/discussion")
    video_to_images(video_dir)

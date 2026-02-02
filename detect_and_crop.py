from ultralytics import YOLO
import cv2
import os
from pathlib import Path
from tqdm import tqdm

MODEL_PATH = "models/yolov12n-face.pt"
INPUT_ROOT = "frames"
OUTPUT_ROOT = "faces_raw"

model = YOLO(MODEL_PATH)
os.makedirs(OUTPUT_ROOT, exist_ok=True)

images = list(Path(INPUT_ROOT).rglob("*.jpg"))
print("Total frames found:", len(images))

count = 0

for img_path in tqdm(images):
    img = cv2.imread(str(img_path))
    if img is None:
        continue

    results = model(img, conf=0.35, verbose=False)

    if results[0].boxes is None:
        continue

    for box in results[0].boxes.xyxy:
        x1, y1, x2, y2 = map(int, box)

        # clamp bounds
        h, w = img.shape[:2]
        x1, y1 = max(0,x1), max(0,y1)
        x2, y2 = min(w,x2), min(h,y2)

        face = img[y1:y2, x1:x2]
        if face.size == 0:
            continue

        face = cv2.resize(face, (256,256))
        out = f"{OUTPUT_ROOT}/face_{count:06d}.jpg"
        cv2.imwrite(out, face)
        count += 1

print("Done. Faces saved:", count)


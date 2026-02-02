from PIL import Image, UnidentifiedImageError
import imagehash
import os

# Folder where your cropped frames are stored
folder = "faces_raw"

hashes = {}
removed = 0
skipped = 0

for file in os.listdir(folder):
    path = os.path.join(folder, file)

    # Skip non-image files just in case
    if not file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', 
'.gif')):
        skipped += 1
        continue

    try:
        img = Image.open(path)
        h = imagehash.phash(img)
    except (OSError, UnidentifiedImageError):
        print(f"Skipped corrupted or unreadable image: {file}")
        skipped += 1
        continue

    if h in hashes:
        os.remove(path)
        removed += 1
        print(f"Removed duplicate: {file}")
    else:
        hashes[h] = file

print("\n--- Deduplication Summary ---")
print(f"Removed duplicates: {removed}")
print(f"Skipped files (corrupt/non-image): {skipped}")
print(f"Remaining unique images: {len(hashes)}")


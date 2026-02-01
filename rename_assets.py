import os
import glob

# Path to images directory
images_dir = r"c:\Users\Pablo\Documents\trae_projects\Dra Erika WebPage\images"

# List all files
files = os.listdir(images_dir)

# Define mapping logic
video_file = "TRADUCCIÓN GRINGO LOGO ERIKA.mp4"
profile_candidate = "WhatsApp Image 2025-07-16 at 12.29.03 PM.jpeg"

# Counters
gallery_count = 1

print(f"Processing {len(files)} files...")

for filename in files:
    old_path = os.path.join(images_dir, filename)
    
    # Skip if it's a directory
    if os.path.isdir(old_path):
        continue
        
    new_filename = ""
    
    if filename == video_file:
        new_filename = "promo-video.mp4"
    elif filename == profile_candidate:
        new_filename = "profile.jpg"
    elif filename.lower().endswith(('.jpeg', '.jpg', '.png')):
        new_filename = f"gallery-{gallery_count}.jpg"
        gallery_count += 1
    else:
        print(f"Skipping unknown file type: {filename}")
        continue
        
    new_path = os.path.join(images_dir, new_filename)
    
    # Rename
    try:
        os.rename(old_path, new_path)
        print(f"Renamed: {filename} -> {new_filename}")
    except Exception as e:
        print(f"Error renaming {filename}: {e}")

print("Done.")

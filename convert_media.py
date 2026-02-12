import os
import subprocess
from PIL import Image
from pillow_heif import register_heif_opener
import imageio_ffmpeg

# Register HEIF opener with Pillow
register_heif_opener()

def convert_heic_to_jpg(images_dir):
    for filename in os.listdir(images_dir):
        if filename.lower().endswith(".heic"):
            heic_path = os.path.join(images_dir, filename)
            jpg_filename = os.path.splitext(filename)[0] + ".jpg"
            jpg_path = os.path.join(images_dir, jpg_filename)
            
            print(f"Converting {filename} to {jpg_filename}...")
            try:
                image = Image.open(heic_path)
                image.save(jpg_path, "JPEG", quality=90)
                print(f"Successfully converted {filename}")
            except Exception as e:
                print(f"Error converting {filename}: {e}")

def convert_mov_to_mp4(images_dir):
    ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
    for filename in os.listdir(images_dir):
        if filename.lower().endswith(".mov"):
            mov_path = os.path.join(images_dir, filename)
            mp4_filename = os.path.splitext(filename)[0] + ".mp4"
            mp4_path = os.path.join(images_dir, mp4_filename)
            
            print(f"Converting {filename} to {mp4_filename}...")
            # Use ffmpeg to convert MOV to MP4
            # -i input, -vcodec libx264 (standard for web), -acodec aac, -crf 23 (good quality/size balance)
            cmd = [
                ffmpeg_exe,
                "-i", mov_path,
                "-vcodec", "libx264",
                "-acodec", "aac",
                "-crf", "23",
                "-y", # Overwrite if exists
                mp4_path
            ]
            try:
                subprocess.run(cmd, check=True)
                print(f"Successfully converted {filename}")
            except Exception as e:
                print(f"Error converting {filename}: {e}")

if __name__ == "__main__":
    images_directory = "images"
    print("Starting conversion process...")
    convert_heic_to_jpg(images_directory)
    convert_mov_to_mp4(images_directory)
    print("Conversion process finished.")

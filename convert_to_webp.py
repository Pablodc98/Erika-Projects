import os
from PIL import Image

def convert_to_webp(directory):
    for filename in os.listdir(directory):
        if filename.lower().endswith((".jpg", ".jpeg")):
            input_path = os.path.join(directory, filename)
            # Replace extension while keeping the rest of the filename
            # Note: We need to handle filenames carefully to avoid double extensions or issues with dots
            name_without_ext = os.path.splitext(filename)[0]
            output_filename = name_without_ext + ".webp"
            output_path = os.path.join(directory, output_filename)
            
            print(f"Converting {filename} to {output_filename}...")
            try:
                with Image.open(input_path) as img:
                    # Convert to RGB if necessary (WebP usually handles RGBA but better safe)
                    if img.mode in ("RGBA", "P"):
                        img = img.convert("RGBA")
                    else:
                        img = img.convert("RGB")
                    
                    img.save(output_path, "WEBP", quality=80, method=6)
                print(f"Successfully converted: {output_filename}")
            except Exception as e:
                print(f"Error converting {filename}: {e}")

if __name__ == "__main__":
    images_dir = "images"
    if os.path.exists(images_dir):
        convert_to_webp(images_dir)
    else:
        print(f"Directory {images_dir} not found.")

import os
from PIL import Image, ImageDraw, ImageOps

def create_circular_favicon(input_path, output_png_path, output_ico_path):
    print(f"Processing {input_path}...")
    try:
        with Image.open(input_path) as img:
            # Convert to RGBA to support transparency
            img = img.convert("RGBA")
            
            # Crop to square
            width, height = img.size
            size = min(width, height)
            left = (width - size) // 2
            top = (height - size) // 2
            right = (width + size) // 2
            bottom = (height + size) // 2
            img = img.crop((left, top, right, bottom))
            
            # Create a circular mask
            mask = Image.new('L', (size, size), 0)
            draw = ImageDraw.Draw(mask)
            draw.ellipse((0, 0, size, size), fill=255)
            
            # Apply the mask
            output = Image.new('RGBA', (size, size), (0, 0, 0, 0))
            output.paste(img, (0, 0), mask=mask)
            
            # Resize for favicon.png (keeping it high quality, e.g., 512x512)
            png_output = output.resize((512, 512), Image.Resampling.LANCZOS)
            png_output.save(output_png_path, "PNG")
            print(f"Successfully created: {output_png_path}")
            
            # Create .ico version (multiple sizes)
            ico_sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
            output.save(output_ico_path, format='ICO', sizes=ico_sizes)
            print(f"Successfully created: {output_ico_path}")
            
    except Exception as e:
        print(f"Error creating circular favicon: {e}")

if __name__ == "__main__":
    logo_path = os.path.join("images", "logo-erika.webp")
    if os.path.exists(logo_path):
        create_circular_favicon(logo_path, "favicon.png", "favicon.ico")
    else:
        # Fallback to .jpg if .webp is not there (though it should be)
        logo_path_jpg = os.path.join("images", "logo-erika.jpg")
        if os.path.exists(logo_path_jpg):
            create_circular_favicon(logo_path_jpg, "favicon.png", "favicon.ico")
        else:
            print(f"Logo not found in images directory.")

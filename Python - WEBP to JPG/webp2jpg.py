from pathlib import Path
from PIL import Image

# Set your folder path here (the current directory is ".").
# TODO: Replace this placeholder with the folder containing the WebP files.
folder_path = Path(r"<WEBP_FOLDER>")

# Counter for tracking conversions
converted_count = 0

# Loop through all files and filter specifically for webp extensions
for img_path in folder_path.iterdir():
  if img_path.is_file() and img_path.suffix.lower() == ".webp":
    try:
      with Image.open(img_path) as img:
        # Convert RGBA/P images to RGB (JPEG doesn't support transparency)
        if img.mode in ("RGBA", "P"):
          img = img.convert("RGB")

        # Create the new filename with .jpg extension
        new_path = img_path.with_suffix(".jpg")
        
        # Save as JPEG with high quality (95)
        img.save(new_path, "JPEG", quality=95)
        print(f"Converted: {img_path.name} -> {new_path.name}")
        converted_count += 1
        
    except Exception as e:
      print(f"Failed to convert {img_path.name}: {e}")

print(f"\nDone! Successfully converted {converted_count} WebP file(s).")
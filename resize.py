import os
from PIL import Image

# Input folder containing images
input_folder = "input_images"

# Output folder to save resized images
output_folder = "output_images"

# Resize size
new_size = (300, 300)

# Create output folder if not exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through all files in folder
for filename in os.listdir(input_folder):
    
    file_path = os.path.join(input_folder, filename)
    
    try:
        with Image.open(file_path) as img:
            
            # Resize image
            resized_img = img.resize(new_size)
            
            # Convert to JPG format
            new_filename = os.path.splitext(filename)[0] + ".jpg"
            save_path = os.path.join(output_folder, new_filename)
            
            resized_img.save(save_path, "JPEG")
            
            print(f"Processed: {filename}")
    
    except Exception as e:
        print(f"Skipped {filename}: {e}")

print("✅ All images processed successfully!")
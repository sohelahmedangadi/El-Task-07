# 🖼️ Image Resizer and JPG Converter

A simple Python script that automatically resizes all images from an input folder, converts them to JPG format, and saves them in an output folder.

## 📌 Features

- Resize multiple images in one go
- Convert images to JPG format
- Automatically creates the output folder if it doesn't exist
- Skips unsupported or corrupted files without stopping the program
- Easy to customize image size

---

## 📂 Project Structure

```
Image-Resizer/
│
├── input_images/          # Place original images here
├── output_images/         # Resized JPG images will be saved here
├── image_resizer.py       # Main Python script
├── requirements.txt       # Required Python package
└── README.md
```

---

## ⚙️ Requirements

- Python 3.x
- Pillow Library

Install Pillow using:

```bash
pip install pillow
```

Or install from requirements.txt

```bash
pip install -r requirements.txt
```

---

## 📦 requirements.txt

```
Pillow
```

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/image-resizer.git
```

### 2. Navigate to the project

```bash
cd image-resizer
```

### 3. Add images

Place all images inside the **input_images** folder.

Supported formats include:

- JPG
- JPEG
- PNG
- BMP
- GIF
- TIFF
- WebP (if supported by Pillow)

### 4. Run the script

```bash
python image_resizer.py
```

---

## 📥 Output

The resized images will be saved inside:

```
output_images/
```

All output images are:

- Resized to **300 × 300 pixels**
- Saved in **JPG** format

Example:

```
input_images/
    flower.png
    cat.jpeg
    sunset.bmp

↓

output_images/
    flower.jpg
    cat.jpg
    sunset.jpg
```

---

## 🛠 Customization

You can change the output image size by modifying:

```python
new_size = (300, 300)
```

Example:

```python
new_size = (500, 500)
```

You can also change:

```python
input_folder = "input_images"
output_folder = "output_images"
```

to use different directories.

---

## ❗ Error Handling

The script automatically:

- Skips unsupported files
- Skips corrupted images
- Displays the error message
- Continues processing remaining images

Example:

```
Processed: cat.png
Processed: flower.jpeg
Skipped: notes.txt (cannot identify image file)
```

---

## 📸 Example

Before:

```
input_images/
├── dog.png
├── mountain.jpeg
├── flower.bmp
```

After:

```
output_images/
├── dog.jpg
├── mountain.jpg
├── flower.jpg
```

---

## 📚 Technologies Used

- Python
- Pillow (PIL)
- OS Module

---

## 👨‍💻 Author

**Sohail Ahmed**

---

## 📄 License

This project is open-source and available under the MIT License.

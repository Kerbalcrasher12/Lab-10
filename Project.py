import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from PIL import Image

def convert_to_grayscale():
    input_dir = "Midterm"
    output_dir = os.path.join(input_dir, "output_pngs")
    os.makedirs(output_dir, exist_ok=True)

    filenames = ["Picture1.jpg", "Picture2.jpg", "Picture3.jpg", "Picture4.jpg"]

    for filename in filenames:
        img = Image.open(os.path.join(input_dir, filename))
        img = img.convert("L")
        png_name = filename.replace(".jpg", ".png")
        img.save(os.path.join(output_dir, png_name))
        print("Saved: " + png_name)

convert_to_grayscale()

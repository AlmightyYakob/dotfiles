import os
from PIL import Image

WALLPAPER_DIR = os.path.expandvars("$HOME/wallpapers")

files = os.listdir(WALLPAPER_DIR)
head_jpg_files = [
    os.path.join(WALLPAPER_DIR, file)
    for file in files
    if file.split(".")[-1] in ["jpg", "jpeg"]
]

for file in head_jpg_files:
    print("Current file: " + file)
    png_file = ".".join(file.split(".")[:-1] + ["png"])
    if png_file not in files:
        Image.open(file).save(png_file)

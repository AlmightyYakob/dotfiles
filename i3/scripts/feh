#!/usr/bin/env python3

import os
import subprocess
import random

WALLPAPER_DIR = os.path.abspath(os.path.expandvars("$HOME/wallpapers"))

files = os.listdir(WALLPAPER_DIR)
valid_images = [file for file in files if file.split(".")[-1] == "png"]

file = valid_images[random.randint(0, len(valid_images) - 1)]
print(file)
subprocess.run(["feh", "--bg-fill", f"{WALLPAPER_DIR}/{file}"])

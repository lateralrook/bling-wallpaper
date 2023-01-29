import os
import sys
from wallpaper import set_wallpaper

# Path to directory containing images
image_dir = "path/to/folder"

# List all files in the directory
files = os.listdir(image_dir)

# Filter list to only include image files
image_files = [f for f in files if f.endswith(".jpg") or f.endswith(".jpeg") or f.endswith(".png")]

# Get the most recent image file
most_recent = max(image_files, key=lambda x: os.path.getctime(os.path.join(image_dir, x)))

# Set the most recent image as the wallpaper
set_wallpaper(os.path.join(image_dir, most_recent))

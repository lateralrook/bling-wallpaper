import os
import glob
import ctypes

def set_wallpaper(img_path):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, img_path, 0)

img_folder = r"path/to/folder"
all_imgs = glob.glob(os.path.join(img_folder, "*.jpg"))
most_recent_img = max(all_imgs, key=os.path.getctime)
set_wallpaper(most_recent_img)

# Bling Wallpaper Downloader & Setter
A set of scripts to download the daily Bing wallpapers and set the most recent one as your desktop background.

## Features

- Downloads the highest quality images available
- Downloads the daily wallpapers from the last 5 days
- Saves the images with the date as the file name
- Easy to use
- Works on Windows

## Dependencies
The script requires the following packages to be installed:
- requests
- Pillow

## Usage
1. Clone this repository to your local machine
2. Run `python wallpaperdl.py` to download the wallpapers for the last 5 days
   - The wallpapers will be saved in the same directory as the script with the date as the file name.
4. Edit `setwallpaper.py` to change the "path/to/folder" variable to the directory of the images. 
5. Run `python setwallpaper.py` to set the most recent wallpaper as your desktop background
6. Optionally, use Task Scheduler (Windows) to run these scripts daily
   - Make sure to have wallpaperdl.py run BEFORE setwallpaper.py, otherwise you'll have a black background.

## Motivation
The default Bing wallpaper application adds a watermark over the images and is both slow and annoying. This script was created as a solution to this problem.

## Note

This script is intended for personal use only. Please respect the copyright of the images and do not use them for commercial purposes without obtaining proper permission.

Feel free to fork, modify and distribute this script. If you have any suggestions or improvements, please open an issue or submit a pull request.

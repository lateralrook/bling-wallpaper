# Bling Wallpaper Downloader & Setter
A set of scripts to download the daily Bing wallpapers and set the most recent one as your desktop background.

## Dependencies
The script requires the following packages to be installed:
- requests
- Pillow

## Usage
1. Clone this repository to your local machine
2. Run `python wallpaperdl.py` to download the wallpapers for the last 5 days
3. Edit `setwallpaper.py` to change the "path/to/folder" variable to the directory of the images. 
4. Run `python setwallpaper.py` to set the most recent wallpaper as your desktop background
5. Optionally, use Task Scheduler (Windows) to run this script daily

## Motivation
The default Bing wallpaper application adds a watermark over the images and is both slow and annoying. This script was created as a solution to this problem.

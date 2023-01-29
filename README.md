# Bing Wallpaper Downloader & Setter
A simple script to download the daily Bing wallpapers and set the most recent one as your desktop background.

## Dependencies
The script requires the following packages to be installed:
- requests
- Pillow

## Usage
1. Clone this repository to your local machine
2. Edit both of the scripts to change the "image_dir" variable to the directory of the images.
3. Run `python wallpaperdl.py` to download the wallpapers for the last 5 days
4. Run `python setwallpaper.py` to set the most recent wallpaper as your desktop background
5. Optionally, use Task Scheduler (Windows) to run this script daily

## Motivation
The default Bing wallpaper application adds a watermark over the images, which is both slow and annoying. This script was created as a solution to this problem.

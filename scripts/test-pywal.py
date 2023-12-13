#!python3
import pywal

from icecream import ic

from pywal import colors

bg_image = pywal.wallpaper.get()
colors = pywal.colors.get(bg_image, sat="0.5")
PyWal = [
    [colors["special"]["background"], colors["special"]["background"]],  # background
    [colors["special"]["foreground"], colors["special"]["foreground"]],  # foreground
    [colors["colors"]["color1"], colors["colors"]["color1"]],  # color01
    [colors["colors"]["color2"], colors["colors"]["color2"]],  # color02
    [colors["colors"]["color3"], colors["colors"]["color3"]],  # color03
    [colors["colors"]["color4"], colors["colors"]["color4"]],  # color04
    [colors["colors"]["color5"], colors["colors"]["color5"]],  # color05
    [colors["colors"]["color6"], colors["colors"]["color6"]],  # color06
    [colors["colors"]["color15"], colors["colors"]["color15"]],  # color15
]
ic(PyWal)

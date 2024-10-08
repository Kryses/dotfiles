#!/bin/zsh
#   ___ _____ ___ _     _____   ____  _             _    
#  / _ \_   _|_ _| |   | ____| / ___|| |_ __ _ _ __| |_  
# | | | || |  | || |   |  _|   \___ \| __/ _` | '__| __| 
# | |_| || |  | || |___| |___   ___) | || (_| | |  | |_  
#  \__\_\|_| |___|_____|_____| |____/ \__\__,_|_|   \__| 
#                                                        
#  
# by Stephan Raabe (2023) 
# ----------------------------------------------------- 

# My screen resolution
#xrandr --rate 120

# For Virtual Machine 
# xrandr --output -1 --mode 1920x1080

# Set keyboard layout in config.py
~/scripts/map-tablet.sh

# Load picom
picom &

# Load power manager
xfce4-power-manager &

# Load notification service
dunst &
blueman-applet &
nm-applet &
pamac-tray &
flameshot &
kdeconnect-indicator &
pa-applet &
alacritty -e "znew terminal" &
obsidian &


# Launch polybar
~/dotfiles/qtile/scripts/x11/loadbar.sh

sleep 1

# Setup Wallpaper and update colors
~/dotfiles/qtile/scripts/x11/wallpaper.sh init

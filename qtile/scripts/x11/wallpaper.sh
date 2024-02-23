#!/bin/bash
#   ____ _                              _____ _                          
#  / ___| |__   __ _ _ __   __ _  ___  |_   _| |__   ___ _ __ ___   ___  
# | |   | '_ \ / _` | '_ \ / _` |/ _ \   | | | '_ \ / _ \ '_ ` _ \ / _ \ 
# | |___| | | | (_| | | | | (_| |  __/   | | | | | |  __/ | | | | |  __/ 
#  \____|_| |_|\__,_|_| |_|\__, |\___|   |_| |_| |_|\___|_| |_| |_|\___| 
#                          |___/                                         
#  
# by Stephan Raabe (2023) 
# ----------------------------------------------------- 

case $1 in

    # Load wallpaper from .cache of last session 
    "init")
        if [ -f ~/.cache/current_wallpaper.jpg ]; then
            wal -q -i ~/.cache/current_wallpaper.jpg
            xwallpaper --center ~/.cache/current_wallpaper.jpg
        else
            wallpaper_path=$(find ~/wallpaper -type f | shuf -n 1)    
            wal -q -i $wallpaper_path
            xwallpaper --center $wallpaper_path
        fi
    ;;

    # Select wallpaper with rofi
    "select")
        selected=$(ls -1 ~/wallpaper | grep "jpg" | rofi -dmenu -replace -config ~/dotfiles/rofi/config-wallpaper.rasi)
        if [ ! "$selected" ]; then
            echo "No wallpaper selected"
            exit
        fi
        wallpaper_path=~/wallpaper/$selected
        wal -q -i $wallpaper_path
        xwallpaper --center $wallpaper_path
    ;;

    # Randomly select wallpaper 
    *)
        wallpaper_path=$(find ~/wallpaper -type f | shuf -n 1)    
        wal -q -i $wallpaper_path
        xwallpaper --center $wallpaper_path
    ;;

esac

# ----------------------------------------------------- 
# Reload qtile to color bar
# ----------------------------------------------------- 
qtile cmd-obj -o cmd -f reload_config

# ----------------------------------------------------- 
# Get new theme
# ----------------------------------------------------- 
source "$HOME/.cache/wal/colors.sh"
echo "Wallpaper: $wallpaper"
newwall=$(echo $wallpaper | sed "s|$HOME/wallpaper/||g")

# ----------------------------------------------------- 
# Copy selected wallpaper into .cache folder
# ----------------------------------------------------- 
cp $wallpaper ~/.cache/current_wallpaper.jpg

sleep 1

# ----------------------------------------------------- 
# Send notification
# ----------------------------------------------------- 
notify-send "Colors and Wallpaper updated" "with image $newwall"
echo "Done."

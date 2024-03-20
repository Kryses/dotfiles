#!/bin/zsh
xrandr --output DP-1-4 --preferred --primary &&
xrandr --output DP-1-2 --preferred --below DP-1-4 &&
xrandr --output eDP-1 --preferred --left-of DP-1-4 &&
reload-qtile.sh &&
map-tablet.sh


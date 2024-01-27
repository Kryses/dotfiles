#!/bin/zsh
xrandr --output eDP-1 --off &&
xrandr --output DP-3 --mode 5120x1440 --rate 240 --primary &&
xrandr --output DP-2 --mode 2560x1440 --below DP-3 &&
reload-qtile.sh &&
map-tablet.sh


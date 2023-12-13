#!/usr/bin/zsh

#check screen setup
monitor_setup=$(autorandr --current)
if [[ "$monitor_setup" == "docked" ]]; then
  $HOME/scripts/map-tablet &
fi
export PATH="$PATH:$HOME/scripts"
export EDITOR="nvim"

alacritty &
alacritty -e 'notes' &
alacritty -e 'vit-standalone' &
qutebrowser &
spotify &
discord &

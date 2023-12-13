#!/usr/bin/zsh

monitor_setup=$(autorandr --current)
if [[ "$monitor_setup" == "docked" ]]; then
  xsetwacom set 'Wacom Cintiq Pro 24 Pen stylus' MapToOutput 'DP-2'
  xsetwacom set 'Wacom Cintiq Pro 24 Pen eraser' MapToOutput 'DP-2'
fi

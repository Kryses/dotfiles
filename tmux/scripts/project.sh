#!/run/current-system/sw/bin/bash

if [ $(timew get dom.active) -eq 1 ]; then
  echo $(timew | grep -oP 'project\|\K[^"]+' | cut -c 1-30)
fi

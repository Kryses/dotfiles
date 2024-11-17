#!/run/current-system/sw/bin/bash

if [ $(timew get dom.active) -eq 1 ]; then
  echo "green"
else
  echo "cyan"
fi

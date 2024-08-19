if [ $(timew get dom.active) -eq 1 ]; then
  echo 📝 $(timew | grep -oP '"task\|\K[^"]+' | cut -c 1-30)...
else
  echo ""
fi

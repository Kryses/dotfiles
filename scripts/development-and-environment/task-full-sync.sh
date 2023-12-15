export DISPLAY=:0 
export DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/$(id -u)/bus
notify-send "Starting Task Sync" "Starting bug warrior and task server sync"
/home/kryses/scripts/task-pull.sh 
/home/kryses/scripts/task-clean.sh 
/home/kryses/scripts/task-sync.sh
notify-send "Finished Task Sync" "Finished bug warrior and task server sync"

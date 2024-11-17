#!/run/current-system/sw/bin/bash

OVERDUE_ICON=''
DUE_ICON='󱑁'
SCHEDULED_ICON='󰔠'
INBOX_ICON='󰋻'

overdue_tasks=$(task count +OVERDUE)
due_today=$(task count due.before:eow +READY)
scheduled=$(task count scheduled.before:eow +READY)
inbox=$(task count "(reviewed.none: or reviewed.before:now-6days) and (+PENDING or +WAITING)")


return_string=""
if [ ! $overdue_tasks -eq 0 ]; then return_string="$OVERDUE_ICON $overdue_tasks"

fi

if [ ! $due_today -eq 0 ]; then 
  return_string="$return_string $DUE_ICON $due_today"

fi

if [ ! $scheduled -eq 0 ]; then 
  return_string="$return_string $SCHEDULED_ICON $scheduled"
fi
echo -e $return_string

if [ ! $inbox -eq 0 ]; then 
  return_string="$return_string $INBOX_ICON $inbox"
fi
echo -e $return_string


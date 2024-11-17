#!/run/current-system/sw/bin/bash

NOTIFICATION_ICON='󰛏'
PULL_REQUESTS_ICON='󰓂'

all_notifications=$(gh api notifications)
notifications=$(echo "$all_notifications" | jq 'keys | length')
pull_requests=$(echo "$all_notifications" | jq '[.[] | select(.subject.type == "PullRequest")] | length')
return_string=""
if [ ! "$notifications" -eq 0 ]; then
  return_string="$NOTIFICATION_ICON $notifications"
fi

if [ ! "$pull_requests" -eq 0 ]; then
  return_string="$return_string $PULL_REQUESTS_ICON $pull_requests"
fi

echo -e "$return_string"

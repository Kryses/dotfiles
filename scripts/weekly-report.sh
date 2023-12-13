#!/usr/bin/zsh
echo '___'
echo '@code'
toilet -f big 'Burndown'
task burndown.daily 
echo '@end'
echo ''
echo '___'

echo '___'
echo '@code'
toilet -f big 'Tasks'
echo ''
echo '___'
task rc.report.completed.columns=project,description.count,end \
  rc.report.completed.labels=project,description,end \
  completed end.after:$(date -d 'last week' +'%Y-%m-%dT00:00:00') end.before:$(date +'%Y-%m-%dT00:00:00')
echo '@end'
echo ''
echo '___'



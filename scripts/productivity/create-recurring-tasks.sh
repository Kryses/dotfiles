#!/usr/bin/zsh

tasks=(
    "project:home 'make bed' size:L priority:H due:10am recur:daily wait:6am +HAB +MRN"
    "project:home 'brush teeth' size:L priority:H due:10am recur:daily wait:6am +HAB +MRN"
    "project:home 'walk' size:L priority:H due:10am recur:daily wait:6am +HAB +MRN"
    "project:home 'feed rabbits' size:L priority:H due:10am recur:daily wait:6am +HAB +MRN"
    "project:home 'shower' size:L priority:H due:10am recur:daily wait:6am +HAB +MRN"
    "project:home 'make dinner' size:L priority:H due:11pm recur:daily wait:7pm +HAB +NTG"
    "project:home 'brush teeth' size:L priority:H due:11pm recur:daily wait:7pm +HAB +NTG"
    "project:home 'feed rabbits' size:L priority:H due:11pm recur:daily wait:7pm +HAB +NTG"
    "project:home 'brush tina' size:L priority:H due:11pm recur:daily wait:7pm +HAB +NTG"
    "project:home 'journal' size:L priority:H due:11pm recur:daily wait:7pm +HAB +NTG"
    "project:home 'sleep' size:L priority:H due:11pm recur:daily wait:10pm +HAB +NTG +SLEEP"
    "project:home 'vacuum room' size:L priority:H due:11pm recur:3days wait:7pm +HAB +NTG"
    "project:home 'clean rabbit cage' size:L priority:H due:11pm recur:3days wait:7pm +HAB +NTG"
    "project:work 'standup' size:L priority:H due:11pm recur:weekdays wait:7pm +WK +MEETING"
)
echo "${tasks[@]}"


task status:recurring delete

echo "Creating recurring tasks..."
for task in "${tasks[@]}"; do
    echo "Adding task: $task"
    eval "task add $task"
done


#!/usr/bin/zsh

tasks=(
    "project:home 'make bed' size:L priority:H due:10am recur:daily wait:due-1hr until:11:59pm +habit"
    "project:home 'brush teeth' size:L priority:H due:10am recur:daily wait:due-1hr until:11:59pm +habit"
    "project:home 'walk' size:L priority:H due:10am recur:daily wait:due-1hr until:11:59pm +habit"
    "project:home 'feed rabbits' size:L priority:H due:10am recur:daily wait:due-1hr until:11:59pm +habit"
    "project:home 'shower' size:L priority:H due:10am recur:daily wait:due-1hr until:11:59pm +habit"
    "project:home 'make dinner' size:L priority:H due:11pm recur:daily wait:due-1hr until:11:59pm +habit"
    "project:home 'brush teeth' size:L priority:H due:11pm recur:daily wait:due-1hr until:11:59pm +habit"
    "project:home 'feed rabbits' size:L priority:H due:11pm recur:daily wait:due-1hr until:11:59pm +habit"
    "project:home 'brush tina' size:L priority:H due:11pm recur:daily wait:due-1hr until:11:59pm +habit"
    "project:home 'journal' size:L priority:H due:11pm recur:daily wait:due-1hr until:11:59pm +habit"
    "project:home 'sleep' size:L priority:H due:11pm recur:daily wait:10pm until:11:59pm +habit +sleep"
    "project:home 'vacuum room' size:L priority:H due:11pm recur:3days wait:due-1hr until:11:59pm +habit"
    "project:home 'clean rabbit cage' size:L priority:H due:11pm recur:3days wait:due-1hr until:11:59pm +habit"
)
echo "${tasks[@]}"


task status:recurring delete

echo "Creating recurring tasks..."
for task in "${tasks[@]}"; do
    echo "Adding task: $task"
    eval "task add $task"
done


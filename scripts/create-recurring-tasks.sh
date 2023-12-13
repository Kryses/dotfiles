#!/usr/bin/zsh

morning_tasks=(
    "make bed"
    "brush teeth"
    "walk"
    "feed rabbits"
    "shower"
)

night_tasks=(
    "make dinner"
    "brush teeth"
    "feed rabbits"
    "brush tina"
    "journal"
    "sleep"
)
threeday_tasks=(
    "vacuum room"
    "clean rabbit cage"
)

sunday_tasks=(
  "review inbox"
  "generate weekly report"
)

work_daily_meetings=(
  "standup"
)

task status:recurring delete

echo "Creating recurring tasks..."
echo "Morning tasks: ${morning_tasks[@]}"
for task in "${morning_tasks[@]}"; do
    task add project:home description: "$task" size:L priority:H due:10am recur:daily wait:6am +HAB +MRN
done

echo "Night tasks: ${night_tasks[@]}"
for task in "${night_tasks[@]}"; do
    task add project:home description: "$task" size:L priority:H due:11pm recur:daily wait:10pm +HAB +NTE
done

echo "3 day tasks: ${threeday_tasks[@]}"
for task in "${threeday_tasks[@]}"; do
    task add project:home description: "$task" size:L priority:H due:10pm recur:3days wait:6am +HAB 
done

echo "Sunday tasks: ${sunday_tasks[@]}"
for task in "${sunday_tasks[@]}"; do
    task add project:home description: "$task" size:L priority:H due:sunday recur:weekly wait:sunday +HAB 
done

echo "Work daily meetings: ${work_daily_meetings[@]}"
for task in "${work_daily_meetings[@]}"; do
    task add project:work description: "$task" size:L priority:H due:'12:15pm' recur:daily wait:12pm +HAB +WRK +MTG
done

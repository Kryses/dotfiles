if [ $(timew get dom.active) -eq 1 ]; then
	tasktime="$(timew get dom.active.duration | grep -Eo '[0-9]+[A-Z]' | head -n 1 | tr 'A-Z' 'a-z')"
	echo "$tasktime"
fi


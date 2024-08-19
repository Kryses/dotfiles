# Print the current date.

TMUX_POWERLINE_SEG_DATE_FORMAT_DEFAULT="%F"

generate_segmentrc() {
	read -d '' rccontents  << EORC
# date(1) format for the date. If you don't, for some reason, like ISO 8601 format you might want to have "%D" or "%m/%d/%Y".
export TMUX_POWERLINE_SEG_DATE_FORMAT="${TMUX_POWERLINE_SEG_DATE_FORMAT_DEFAULT}"
EORC
	echo "$rccontents"
}

__process_settings() {
	if [ -z "$TMUX_POWERLINE_SEG_DATE_FORMAT" ]; then
		export TMUX_POWERLINE_SEG_DATE_FORMAT="${TMUX_POWERLINE_SEG_DATE_FORMAT_DEFAULT}"
	fi
}

run_segment() {
        __process_settings
        if [ $(timew get dom.active) -eq 1 ]; then
  					echo \  $(timew | grep -oP 'project\|\K[^"]+' | cut -c 1-30)
  			fi
	return 0
}

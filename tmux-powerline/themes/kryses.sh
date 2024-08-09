####################################################################################################
# This is a bubble theme created by @embe221ed (https://github.com/embe221ed)
# colors are inspired by catppuccin palettes (https://github.com/catppuccin/catppuccin)
####################################################################################################

# COLORS

# background for frappe catppuccin terminal theme
theme_background="#24273a"
theme_forground="#eeeee4"

# background for macchiato catppuccin terminal theme
# thm_bg="#24273A"

theme_gray="#414559"
theme_light="#154cFF"
theme_dark="#154c79"
teal="#81c8be"
surface0="#414559"
eggplant="#154c79"
spotify_green="#1db954"
spotify_black="#191414"
thm_orange="#f5a97f"


TMUX_POWERLINE_SEPARATOR_LEFT_BOLD=""
TMUX_POWERLINE_SEPARATOR_LEFT_THIN=""
TMUX_POWERLINE_SEPARATOR_RIGHT_BOLD=""
TMUX_POWERLINE_SEPARATOR_RIGHT_THIN=""
TMUX_POWERLINE_SEPARATOR_THIN="|"

TMUX_POWERLINE_DEFAULT_BACKGROUND_COLOR=${TMUX_POWERLINE_DEFAULT_BACKGROUND_COLOR:-$theme_background}
TMUX_POWERLINE_DEFAULT_FOREGROUND_COLOR=${TMUX_POWERLINE_DEFAULT_FOREGROUND_COLOR:-$theme_background}

TMUX_POWERLINE_DEFAULT_LEFTSIDE_SEPARATOR=${TMUX_POWERLINE_DEFAULT_LEFTSIDE_SEPARATOR:-$TMUX_POWERLINE_SEPARATOR_RIGHT_BOLD}
TMUX_POWERLINE_DEFAULT_RIGHTSIDE_SEPARATOR=${TMUX_POWERLINE_DEFAULT_RIGHTSIDE_SEPARATOR:-$TMUX_POWERLINE_SEPARATOR_LEFT_BOLD}

# See man tmux.conf for additional formatting options for the status line.
# The `format regular` and `format inverse` functions are provided as conveinences

if [ -z $TMUX_POWERLINE_WINDOW_STATUS_CURRENT ]; then
	TMUX_POWERLINE_WINDOW_STATUS_CURRENT=(
		"#[$(format regular)]" \
		"$TMUX_POWERLINE_DEFAULT_RIGHTSIDE_SEPARATOR" \
		"#[$(format inverse)]" \
		" #I#F " \
		"$TMUX_POWERLINE_SEPARATOR_THIN" \
		" #W " \
		"#[$(format regular)]" \
		"$TMUX_POWERLINE_DEFAULT_LEFTSIDE_SEPARATOR"
	)
fi

if [ -z $TMUX_POWERLINE_WINDOW_STATUS_STYLE ]; then
	TMUX_POWERLINE_WINDOW_STATUS_STYLE=(
		"$(format regular)"
	)
fi

if [ -z $TMUX_POWERLINE_WINDOW_STATUS_FORMAT ]; then
	TMUX_POWERLINE_WINDOW_STATUS_FORMAT=(
		"#[$(format regular)]" \
		"  #I#{?window_flags,#F, } " \

		"$TMUX_POWERLINE_SEPARATOR_THIN" \
		" #W "
	)
fi

# Format: segment_name background_color foreground_color [non_default_separator] [separator_background_color] [separator_foreground_color] [spacing_disable] [separator_disable]
#
# * background_color and foreground_color. Formats:
#   * Named colors (chech man page of tmux for complete list) e.g. black, red, green, yellow, blue, magenta, cyan, white
#   * a hexadecimal RGB string e.g. #ffffff
#   * 'default' for the defalt tmux color.
# * non_default_separator - specify an alternative character for this segment's separator
# * separator_background_color - specify a unique background color for the separator
# * separator_foreground_color - specify a unique foreground color for the separator
# * spacing_disable - remove space on left, right or both sides of the segment:
#   * "left_disable" - disable space on the left
#   * "right_disable" - disable space on the right
#   * "both_disable" - disable spaces on both sides
#   * - any other character/string produces no change to default behavior (eg "none", "X", etc.)
#
# * separator_disable - disables drawing a separator on this segment, very useful for segments
#   with dynamic background colours (eg tmux_mem_cpu_load):
#   * "separator_disable" - disables the separator
#   * - any other character/string produces no change to default behavior
#
# Example segment with separator disabled and right space character disabled:
# "hostname 33 0 {TMUX_POWERLINE_SEPARATOR_RIGHT_BOLD} 33 0 right_disable separator_disable"
#
# Note that although redundant the non_default_separator, separator_background_color and
# separator_foreground_color options must still be specified so that appropriate index
# of options to support the spacing_disable and separator_disable features can be used

if [ -z $TMUX_POWERLINE_LEFT_STATUS_SEGMENTS ]; then
	TMUX_POWERLINE_LEFT_STATUS_SEGMENTS=(
		# "tmux_session_info $blue $thm_bg" \
		"hostname 236 136" \
		"pwd 235 136" \
		# "ifstat 30 255" \
		#"ifstat_sys 30 255" \
		# "lan_ip $sky_blue $thm_bg ${TMUX_POWERLINE_SEPARATOR_RIGHT_THIN}" \
		#"wan_ip $sky_blue $thm_bg" \
		"vcs_branch $theme_gray" \
		# "vcs_compare 60 255" \
		# "vcs_staged 64 255" \
		#"vcs_modified 9 255" \
		#"vcs_others 245 0" \
	)
fi

if [ -z $TMUX_POWERLINE_RIGHT_STATUS_SEGMENTS ]; then
	TMUX_POWERLINE_RIGHT_STATUS_SEGMENTS=(
		# "earthquake 3 0" \
		# "macos_notification_count 29 255" \
		#"mailcount 9 255" \
		"now_playing $spotify_green $spotify_black ${TMUX_POWERLINE_SEPARATOR_LEFT_THIN}" \
		# "cpu 240 136" \
		# "load 237 167" \
		#"rainbarf 0 ${TMUX_POWERLINE_DEFAULT_FOREGROUND_COLOR}" \
		#"xkb_layout 125 117" \
		"project 235 136 ${TMUX_POWERLINE_SEPARATOR_LEFT_BOLD}" \
		"task 236 136 ${TMUX_POWERLINE_SEPARATOR_LEFT_BOLD}" \
		"timew 237 136 ${TMUX_POWERLINE_SEPARATOR_LEFT_BOLD}" \
		"current_tasks 238 136 ${TMUX_POWERLINE_SEPARATOR_LEFT_BOLD}" \
		"date_day 239 136 ${TMUX_POWERLINE_SEPARATOR_LEFT_BOLD}" \
		"date 240 136 ${TMUX_POWERLINE_SEPARATOR_LEFT_THIN}" \
		# "weather 37 255" ${TMUX_POWERLINE_SEPARATOR_LEFT_BOLD} \
		"time 241 136 ${TMUX_POWERLINE_SEPARATOR_LEFT_BOLD}" \
		# "battery $thm_blue  $thm_bg ${TMUX_POWERLINE_SEPARATOR_LEFT_BOLD}" \
	)
fi

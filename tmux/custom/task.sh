show_task() {
  local index=$1
  local icon="$(get_tmux_option "@catppuccin_task_icon" "󰙨")"
  local color="$(get_tmux_option "@catppuccin_task_color" "$thm_blue")"
  local text="$(get_tmux_option "@catppuccin_task_text" "Test")"
  local module=$( build_status_module "$index" "$icon" "$color" "$text" )

  echo "$module"
}


#!/run/current-system/sw/bin/bash
show_task_status() {
  local index=$1
  local icon="$(get_tmux_option "@catppuccin_task_status_icon" "")"
  local color="$(get_tmux_option "@catppuccin_task_status_color" "$thm_yellow")"
  local text="$(get_tmux_option "@catppuccin_task_status_text" "Test")"
  local module=$( build_status_module "$index" "$icon" "$color" "$text" )

  echo "$module"
}

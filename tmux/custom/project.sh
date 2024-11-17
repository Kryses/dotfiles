#!/run/current-system/sw/bin/bash
show_project() {
  local index=$1
  local icon="$(get_tmux_option "@catppuccin_project_icon" "")"
  local color="$(get_tmux_option "@catppuccin_project_color" "$thm_blue")"
  local text="$(get_tmux_option "@catppuccin_project_text" "Test")"
  local module=$( build_status_module "$index" "$icon" "$color" "$text" )

  echo "$module"
}

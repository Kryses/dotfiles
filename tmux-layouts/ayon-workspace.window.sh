window_root "~/work/repos/ayon-workspace"
new_window "ayon-workspace"
run_cmd "poetry run nvim"
split_v 20
run_cmd "poetry shell"
select_pane 0

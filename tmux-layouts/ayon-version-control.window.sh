window_root "~/work/repos/ayon-workspace/addons/ayon-version-control"
new_window "ayon-version-control"
run_cmd "poetry run nvim"
split_v 20
run_cmd "poetry shell"
select_pane 0

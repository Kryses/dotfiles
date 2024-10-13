window_root "~/work/repos/ayon-workspace/addons/ayon-maya-toolkit"
new_window "ayon-maya-toolkit"
run_cmd "nvim"
split_v 20
run_cmd "poetry shell"
split_h 60
run_cmd "cd ./.kryses && ./watch-toolkit.sh"
select_pane 0

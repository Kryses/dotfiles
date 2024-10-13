window_root "~/work/repos/ayon-workspace/addons/halon-slate"
new_window "halon-slate"
run_cmd "nvim"
split_v 20
run_cmd "poetry shell"
split_h 60
run_cmd "cd ./.kryses && ./watch-slate.sh"
select_pane 0

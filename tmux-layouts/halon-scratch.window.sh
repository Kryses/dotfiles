window_root "~/work/repos/scratch"
new_window "scratch"
run_cmd "nvim"
split_v 20
run_cmd "poetry shell"
split_h 60
run_cmd "cd ./.kryses && ./watch-scratch.sh"
select_pane 0

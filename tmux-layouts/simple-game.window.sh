window_root "~/repos/game-dev/simple-game"
new_window "simple-game"
run_cmd "nvim"
split_v 20
run_cmd "poetry shell"
split_h 60
run_cmd "yazi"
select_pane 0

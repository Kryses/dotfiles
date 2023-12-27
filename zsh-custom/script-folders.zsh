script_folders=(
  "development"
  "system"
  "misc"
  "productivity"
  "system"
  "utility"
  )

export PATH="$HOME/.local/bin:/snap/bin:$HOME/.dotfiles/bin:$HOME/scripts:$PATH"
for folder in "${script_folders[@]}"; do
  export PATH="$HOME/scripts/$folder:$PATH"
done

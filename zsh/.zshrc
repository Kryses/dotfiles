bindkey -v
eval "$(starship init zsh)"
export XDG_CONFIG_HOME="$HOME/.config"
export OPENAI_KEY="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"

if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

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

export EDITOR="nvim"
source ~/.local/repos/powerlevel10k/powerlevel10k.zsh-theme
source ~/.nvm/nvm.sh

# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f ~/.zsh-nvm.zsh ]] || source ~/.zsh-nvm.zsh
[[ ! -f ~/.bashrc ]] || source ~/.bashrc

#nnn
source ~/.config/nnn/nnnrc.sh

alias df=~/.dotfiles/bin/dotfiles
alias rz="source ~/.zshrc"
alias op="pass open --timer 10min"
alias gp="pass -c "
alias connect_server='ssh kryses@kryses-dev'
alias tw='timew'
alias t='vit'
alias tw-shift='tw stop && tw start '
alias tws='tw summary'
alias twd='tw day'
alias habit='task rc.data.location=~/.habit'
alias mobile='autorandr -l mobile'
alias docked='autorandr -l docked'
alias docked-wacom='autorandr -l docked-wacom'
alias confz='nvim ~/.zshrc'
alias ac='source ./.venv/bin/activate'
alias work='cd ~/repos/work'


fpath=($HOME/.local/repos/zsh-completions/src $fpath)

#Auto Suggest
export ZSH_AUTOSUGGEST_STRATEGY=(history completion)
source ~/.local/repos/zsh-autosuggestions/zsh-autosuggestions.zsh


nnn_cd()                                                                                                   
{
    if ! [ -z "$NNN_PIPE" ]; then
        printf "%s\0" "0c${PWD}" > "${NNN_PIPE}" !&
    fi  
}

trap nnn_cd EXIT
n ()
{
    # Block nesting of nnn in subshells
    [ "${NNNLVL:-0}" -eq 0 ] || {
        echo "nnn is already running"
        return
    }

    # The behaviour is set to cd on quit (nnn checks if NNN_TMPFILE is set)
    # If NNN_TMPFILE is set to a custom path, it must be exported for nnn to
    # see. To cd on quit only on ^G, remove the "export" and make sure not to
    # use a custom path, i.e. set NNN_TMPFILE *exactly* as follows:
    #      NNN_TMPFILE="${XDG_CONFIG_HOME:-$HOME/.config}/nnn/.lastd"
    export NNN_TMPFILE="${XDG_CONFIG_HOME:-$HOME/.config}/nnn/.lastd"

    # Unmask ^Q (, ^V etc.) (if required, see `stty -a`) to Quit nnn
    # stty start undef
    # stty stop undef
    # stty lwrap undef
    # stty lnext undef

    # The command builtin allows one to alias nnn to n, if desired, without
    # making an infinitely recursive alias
    command nnn "$@"

    [ ! -f "$NNN_TMPFILE" ] || {
        . "$NNN_TMPFILE"
        rm -f "$NNN_TMPFILE" > /dev/null
    }
}
if command -v zoxide > /dev/null; then
  eval "$(zoxide init zsh)"
fi
# Source the Lazyman shell initialization for aliases and nvims selector
# shellcheck source=.config/nvim-Lazyman/.lazymanrc
[ -f ~/.config/nvim-Lazyman/.lazymanrc ] && source ~/.config/nvim-Lazyman/.lazymanrc
# Source the Lazyman .nvimsbind for nvims key binding
# shellcheck source=.config/nvim-Lazyman/.nvimsbind
[ -f ~/.config/nvim-Lazyman/.nvimsbind ] && source ~/.config/nvim-Lazyman/.nvimsbind
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh

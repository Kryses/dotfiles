#------------------------------------------------------------
# Aliases
# ------------------------------------------------------------

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
alias conft='nvim ~/.tmux.conf'
alias ac='source ./.venv/bin/activate'
alias work='cd ~/repos/work'
alias tmux='tmux -2'
alias main='~/scripts/development/open-main.sh'

#------------------------------------------------------------
# Aliases from qtile tutorial
#------------------------------------------------------------
alias c='clear'
alias nf='neofetch'
alias pf='pfetch'
alias ls='eza -al'
alias shutdown='systemctl poweroff'
alias v='nvim'
alias wifi='nmtui'
alias winclass="xprop | grep 'CLASS'"
alias dot="cd ~/dotfiles"

# -----------------------------------------------------
# GIT
# -----------------------------------------------------

alias gs="git status"
alias ga="git add"
alias gc="git commit -m"
alias gp="git push"
alias gpl="git pull"
alias gst="git stash"
alias gsp="git stash; git pull"
alias gcheck="git checkout"


#------------------------------------------------------------
# Scripts
#------------------------------------------------------------


# -----------------------------------------------------
# VIRTUAL MACHINE
# -----------------------------------------------------

alias vm='~/private/launchvm.sh'
alias lg='~/dotfiles/scripts/looking-glass.sh'
alias vmstart='virsh --connect qemu:///system start win11'
alias vmstop='virsh --connect qemu:///system destroy win11'

# -----------------------------------------------------
# EDIT CONFIG FILES
# -----------------------------------------------------

alias confq='nvim ~/dotfiles/qtile/config.py'
alias confp='nvim ~/dotfiles/picom/picom.conf'
alias confb='nvim ~/dotfiles/.bashrc'
alias confz='nvim ~/dotfiles/zsh-custom'
alias conft='nvim ~/dotfiles/.tmux.conf'
alias confn='nvim ~/.config/nvim/lua/user'


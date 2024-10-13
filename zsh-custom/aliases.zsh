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
alias ta='task add'
alias tw-shift='tw stop && tw start '
alias tws='tw summary'
alias twd='tw day'
alias habit='task rc.data.location=~/.habit'
alias mobile='autorandr -l mobile'
alias docked='autorandr -l docked'
alias docked-wacom='autorandr -l docked-wacom'
alias confz='nvim ~/.zshrc'
alias conft='nvim ~/.tmux.conf'
alias ac='source ./venv/bin/activate'
alias tmux='tmux -2'
alias main='~/scripts/development/open-main.sh'
alias kz='zellij kill-all-sessions'
alias halon-up='nmcli connection up Halon'
alias halon-down='nmcli connection down Halon'
alias connect-pipeline="ssh -i $(pass work/hl/aws-ssh)"

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
alias gg="lazygit"
alias y="yazi"


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

alias rt='cd ~/.task && git reset --hard && git pull && cd -'

alias conf-qtile='nvim ~/dotfiles/qtile/config.py'
alias conf-picom='nvim ~/dotfiles/picom/picom.conf'
alias conf-bash='nvim ~/dotfiles/.bashrc'
alias conf-zsh='nvim ~/.zshrc'
alias conf-tmux='nvim ~/dotfiles/tmux/.tmux.conf'
alias conf-task='nvim ~/dotfiles/.taskrc'
alias conf-dot='cd ~/dotfiles && nvim'
alias conf-nvim='cd ~/.config/nvim && nvim'

alias work='cd ~/work/repos'
alias ayon-workspace='cd ~/work/repos/ayon-workspace'


cwork() {
    ssh -o ServerAliveInterval=60 $(pass work/hl/hal-ssh-ip) -i ~/.ssh/id_rsa -p 22 
}
alias workm='sshfs $(pass work/hl/hal-ssh-ip):E:/development ~/repos/work'
prime-run() {
    __NV_PRIME_RENDER_OFFLOAD=1 __VK_LAYER_NV_optimus=NVIDIA_only __GLX_VENDOR_LIBRARY_NAME=nvidia $@
}

work-sync() {
    rsync -e "ssh -p 2222" -rvaz --update --exclude='.git' ~/repos/work/pipeline-workspace $(pass work/hl/hal-ssh-ip):/mnt/e/development
}

export PYENV_ROOT="$HOME/.pyenv"
[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"

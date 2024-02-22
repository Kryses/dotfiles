#!/bin/zsh

cwork() {
    ssh $(pass work/hl/hal-ssh-ip)
}
nmcli connection up Halon 
cwork

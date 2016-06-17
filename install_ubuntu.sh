#!/bin/bash

# Initial Setup

sudo apt-get install -y build-essentials cmake vim tmux

# Python Dev

cp ./.vimrc ~/
cp ./.tmux.conf ~/

curl https://j.mp/spf13-vim3 -L > spf13-vim.sh && sh spf13-vim.sh

wget -O ~/.vim/bundle/vim-colors/colors/wombat256mod.vim http://www.vim.org/scripts/download_script.php?src_id=13400

cp ./.vimrc.local ~/
cp ./.vimrc.before.local ~/
cp ./.vimrc.bundle.local ~/

vim -c '' \
    -c 'BundleInstall!' \
    -c 'qa!'
sudo pip install jedi
sudo pip install rope


# C++ Dev

sudo ~/.vim/bundle/YouCompleteMe/install.sh --clang-completer

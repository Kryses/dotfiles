#!/bin/bash

# Python Dev

cp ./.vimrc ~/
cp ./.tmux.conf ~/

mkdir -p ~/.vim/autoload
curl -so ~/.vim/autoload/pathogen.vim https://raw.githubusercontent.com/tpope/vim-pathogen/master/autoload/pathogen.vim

mkdir -p ~/.vim/colors && cd ~/.vim/colors
wget -O wombat256mod.vim http://www.vim.org/scripts/download_script.php?src_id=13400

mkdir -p ~/.vim/bundle && cd ~/.vim/bundle
git clone https://github.com/Lokaltog/vim-powerline.git
git clone https://github.com/kien/ctrlp.vim.git
git clone https://github.com/klen/python-mode
git clone https://github.com/davidhalter/jedi-vim.git
git clone https://github.com/scrooloose/nerdtree.git

mkdir -p ~/.vim/ftplugin
wget -O ~/.vim/ftplugin/python_editing.vim http://www.vim.org/scripts/download_script.php?src_id=5492

sudo pip install jedi
sudo pip install rope

# C++ Dev

cd ~/.vim/bundle
git clone https://github.com/Valloric/YouCompleteMe.git
cd YouCompleteMe
git submodule update --init --recursive
./install.sh --clang-completer

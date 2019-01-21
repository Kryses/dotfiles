#!/bin/bash

yum -y install gcc-c++ ncurses-devel python-devel
git clone https://github.com/vim/vim.git
cd vim/src && git check v8.0.1522

./configure \
  --disable-nls \
  --enable-cscope \
  --enable-gui=no \
  --enable-multibyte  \
  --enable-pythoninterp \
  --enable-rubyinterp \
  --prefix=$HOME/.local/vim \
  --with-features=huge  \
  --with-python-config-dir=/usr/lib/python2.7/config \
  --with-tlib=ncurses \
  --without-x

make && make install

echo 'if [ -d "$HOME/.local/vim/bin/" ] ; then' >> ~/.bashrc
echo '	PATH="$HOME/.local/vim/bin/:$PATH"' >> ~/.bashrc
echo 'fi' >> ~/.bashrc
source ~/.bashrc

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

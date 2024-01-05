# According to the standard:
# https://zdharma-continuum.github.io/Zsh-100-Commits-Club/Zsh-Plugin-Standard.html
0="${${(M)0:#/*}:-$PWD/$0}"

source ${0:h}/zsh-gpt.zsh

export ZELLIJ_AUTO_ATTACH=true
export ZELLIJ_AUTO_EXIT=true
export OPENAI_KEY="$(pass personal/open-ai-api)"

eval "$(zellij setup --generate-auto-start zsh)"

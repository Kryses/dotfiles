#!/bin/zsh
export OPENAI_KEY="$(pass personal/open-ai-api)"
export OPENAI_API_KEY="$(pass personal/chatgpt-nvim)"
alias chat-ops='chatgpt -m "gpt-4" -i "You are a devops engineer"'
alias chat-dev='chatgpt -m "gpt-4" -i "You are a software engineer"'
alias chat-assist='chatgpt -m "gpt-4" -i "You are a personal assistant"'

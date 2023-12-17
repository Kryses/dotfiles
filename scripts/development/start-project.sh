#!/bin/bash

#  ___ _            _     ___          _        _   
# / __| |_ __ _ _ _| |_  | _ \_ _ ___ (_)___ __| |_ 
# \__ \  _/ _` | '_|  _| |  _/ '_/ _ \| / -_) _|  _|
# |___/\__\__,_|_|  \__| |_| |_| \___// \___\__|\__|
#                                   |__/            

python3 -m venv .venv
touch requirements.txt
touch .gitignore
touch README.md
touch pyproject.toml

echo '.venv/*' >> .gitignore
project_name=$(basename "$PWD")
echo $project_name
cat $HOME/scripts/templates/pyproject-standard.toml | sed 's/{project_name}/'$project_name'/g' >> pyproject.toml

mkdir .kryses
mkdir src
mkdir tests
mkdir tests/fixtures


touch tests/fixtures/__init__.py
touch tests/conftest.py
touch tests/__init__.py

git init
git add --all
git commit -m "Initial commit"


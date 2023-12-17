#!/bin/zsh

BACKUP_DIR=$HOME/.task-backups
mkdir -p $BACKUP_DIR
cd $BACKUP_DIR
tar -cvzf "$(date +'%Y%m%d_%H%M%S').tar.gz" $HOME/.task

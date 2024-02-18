#!/bin/zsh

BACKUP_DIR=$HOME/.task-backups
mkdir -p $BACKUP_DIR
cd $BACKUP_DIR
tar -cvzf "$(date +'%Y%m%d_%H%M%S').tar.gz" $HOME/.task
find $BACKUP_DIR -name "*.tar.gz" ! -name "daily-*" -type f | sort | head -n -4 | xargs rm -f

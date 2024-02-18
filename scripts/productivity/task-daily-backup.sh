#!/bin/zsh
BACKUP_DIR=$HOME/.task-backups
mkdir -p $BACKUP_DIR
cd $BACKUP_DIR
tar -cvzf "daily-$(date +'%Y%m%d_%H%M%S').tar.gz" $HOME/.task
find "$BACKUP_DIR" -name "daily_*tar.gz" -type f -mtime +7 -delete

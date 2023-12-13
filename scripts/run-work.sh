#!/usr/bin/zsh
site_list=(
    "https://outlook.office.com/calendar/view/day"
    "https://outlook.office.com/mail/"
    "https://lucid.app/lucidspark/eadc307a-b1fb-441e-9e6d-40bacdffb3d1/edit?page=0_0&invitationId=inv_b75c19c5-fb47-4323-8f2b-1de37d010c1e#"
    "https://halon.atlassian.net/jira/software/c/projects/ENG/boards/1022?assignee=6112c4bd7ab143006e7d29f1&assignee=5fa032f5f7b30b006e11fdc2"
  )

echo "Opening sites: $site_list"
for site in $site_list; do
  qutebrowser -R --target window $site &
done

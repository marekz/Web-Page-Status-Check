# Web Page Status Check
## Simple script to domain check

Script simple check site code response
If status code is ok - 200 than do nothing.
If status code is different then 200, send email notification to declared in config.ini.

Finally, I add my script to crontab like:

1 * * * * /usr/bin/python3 /home/userdir/scripts/WebPageStatusCheck/main.py >> /home/userdir/scripts/WebPageStatusCheck/log/WebPageStatusCheck.log 2>&1

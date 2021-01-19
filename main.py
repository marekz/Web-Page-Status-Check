from CheckSiteStatus import CheckSiteStatus
from SendMail import SendMail
from datetime import datetime
import configparser


config = configparser.ConfigParser()
config.read("config.ini")
site_list = config.get("URL", "SITE_LIST")
site_list = site_list.split(',')

if __name__ == '__main__':
    for url in site_list:
        page_status = CheckSiteStatus.check_site_url(url)

        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

        if page_status == 200:
            print('{}: Site {} working correctly...'.format(dt_string, url))
        else:
            mail = SendMail(url, page_status)
            mail.send_notification_if_error()
            print('{}: Error occurred on site {}...'.format(dt_string, url))

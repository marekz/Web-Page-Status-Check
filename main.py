from CheckSiteStatus import CheckSiteStatus
from SendMail import SendMail
import configparser


config = configparser.ConfigParser()
site_list = config.get("URL", "SITE_LIST")


if __name__ == '__main__':
    for url in site_list:
        page_status = CheckSiteStatus.check_site_url(url)

        if page_status == 200:
            print('Site {} working correctly...'.format(url))
        else:
            mail = SendMail(url, page_status)
            mail.send_notification_if_error()

import smtplib
import configparser


class SendMail:
    def __init__(self, url, status):
        self.url = url
        self.status = status

        self.config = configparser.ConfigParser()
        self.config.read("config.ini")
        self.recipients = self.config.get("USERS", "USERS_ARRAY").split(",")
        self.username = self.config.get("MAIL_CONFIG", "USERNAME")
        self.password = self.config.get("MAIL_CONFIG", "PASSWORD")
        self.host = self.config.get("MAIL_CONFIG", "SERVER")
        self.port = self.config.get("MAIL_CONFIG", "PORT")

    def send_notification_if_error(self):
        for user in self.recipients:
            try:
                subject = 'SERVER {} DOWN'.format(self.url)
                text = 'Here is a message from python check domains. Your site: {} is down ' \
                       'error code: {}, please check.'.format(self.url, self.status)
                server = smtplib.SMTP_SSL(self.host, 465)
                server.ehlo()
                server.login(self.username, self.password)
                body = '\r\n'.join(['To: %s' % user, 'From: %s' % self.username, 'Subject: %s' % subject, '', text])

                server.sendmail(self.username, [user], body)
                print('email sent')

            except Exception as e:
                print(e)

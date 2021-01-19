import urllib.request


class CheckSiteStatus:
    def __init__(self):
        pass

    @staticmethod
    def check_site_url(url: str):
        url = 'http://' + url
        status = urllib.request.urlopen(url).getcode()
        return status

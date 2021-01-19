import urllib.request
from urllib.error import HTTPError


class CheckSiteStatus:
    def __init__(self):
        pass

    @staticmethod
    def check_site_url(url: str):
        url = 'http://' + url
        try:
            status = urllib.request.urlopen(url).getcode()
            return status
        except HTTPError as e:
            return e

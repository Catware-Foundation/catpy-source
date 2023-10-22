
#
# Catware SmartGet Library
#

from fake_useragent import UserAgent
from requests import get
ua = UserAgent()

def sget(url):
    useragent = ua.random
    res = get(url, headers={"User-Agent": useragent}).text
    return res

import requests
import lxml.html as xhtml
import logging

HEADERS = {
    'user-agent': 'python/miner',
    'connection': 'close'
}

# warning messages for logging
WM_REQ = "'requests.{}' does not exist, 'requests.get' will be used"
WM_DEC = "Decode error for {} is ignored"


class Miner(list):
    """A simple crawler/scraper

    Given a url, Miner will `fetch` the webpage according to a specified method
    with possibly some optional arguments. The response will be passed to
    `Miner.build` to build a dom using `lxml.html`, which will be passed to
    `Miner.parser` for scraping.
        
    Args:
        url (str): url to scrape.
        method (str, optional): request method, default is `get`, which means
            `requests.get` will be used. If `requests` module does not have this
            specified method, a warning will be issued and `requests.get` will
            be used instead.
        **kwargs: optional keyword arguments for requests.
    """
    
    def __init__(self, url, method='get', **kwargs):
        super(list, self).__init__()
        self.url = url
        self.method = method
        self.kwargs = {'headers': HEADERS}
        self.kwargs.update(kwargs)
        self.fetch()

    def parse(self, dom):
        pass

    def build(self, response):
        try:
            data = response.content.decode(response.encoding)
        except UnicodeDecodeError:
            logging.warning(WM_DEC.format(response.url))
            data = response.content.decode(response.encoding, 'ignore')
        dom = xhtml.fromstring(data)
        self.parse(dom)

    def fetch(self):
        try:
            req_api = getattr(requests, self.method)
        except AttributeError:
            logging.warning(WM_REQ.format(self.method))
            req_api = requests.get
        response = req_api(url=self.url, **self.kwargs)
        response.raise_for_status()
        self.build(response)

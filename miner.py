import requests
import lxml.html as xhtml

HEADERS = {
    'User-Agent': "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)",
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}


class Miner(list):
    def __init__(self, url,
                 headers=HEADERS,
                 method='get',
                 payload={},
                 cookies={}):
        self.url = url
        self.headers = headers
        self.method = method
        self.payload = payload
        self.cookies = cookies
        super(list, self).__init__()

        self.fetch()

    def parse(self, dom):
        pass

    def build(self, req):
        data = req.content.decode(req.encoding, 'ignore')
        dom = xhtml.fromstring(data)
        self.parse(dom)

    def fetch(self):
        if self.method == 'get':
            req = requests.get(url=self.url,
                               headers=self.headers,
                               cookies=self.cookies,
                               params=self.payload)
        else:
            req = requests.post(url=self.url,
                                headers=self.headers,
                                cookies=self.cookies,
                                data=self.payload)
        req.raise_for_status()
        self.build(req)

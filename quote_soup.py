# -*- coding: utf-8 -*-

from miner import Miner
from bs4 import BeautifulSoup


class SoupMiner(Miner):
    def build(self, response):
        data = response.content.decode(response.encoding, 'ignore')
        dom = BeautifulSoup(data, 'lxml')
        self.parse(dom)


class QuoteSoup(SoupMiner):
    def parse(self, dom):
        quotes = dom.find_all('div', class_='quote')
        for quote in quotes:
            self.append({
                'text': quote.find('span', class_='text').get_text()[1:-1],
                'author': quote.find('small').get_text()
            })


quotes = QuoteSoup('http://quotes.toscrape.com/')
print(quotes)

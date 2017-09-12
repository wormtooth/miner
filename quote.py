# -*- coding: utf-8 -*-

from miner import Miner


class AuthorMiner(Miner):
    def parse(self, dom):
        birthday = dom.xpath('//span[@class="author-born-date"]/text()')[0]
        desc = dom.xpath(
            '//div[@class="author-description"]/text()')[0].strip()
        self.append({'birthday': birthday, 'desc': desc})


class QuoteMiner(Miner):
    def parse(self, dom):
        texts = dom.xpath('//div[@class="quote"]//span[@class="text"]/text()')
        authors = dom.xpath('//div[@class="quote"]//small/text()')
        links = dom.xpath('//div[@class="quote"]//span/a/@href')
        for text, author, link in zip(texts, authors, links):
            url = 'http://quotes.toscrape.com{}'.format(link)
            self.append({
                'author': author,
                'text': text,
                'info': AuthorMiner(url)
            })


qm = QuoteMiner('http://quotes.toscrape.com/')
for q in qm:
    print(q)

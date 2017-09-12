# -*- coding: utf-8 -*-

from miner import Miner
from multiprocessing.dummy import Pool
import time


class QuoteMiner(Miner):
    def parse(self, dom):
        texts = dom.xpath('//div[@class="quote"]//span[@class="text"]/text()')
        authors = dom.xpath('//div[@class="quote"]//small/text()')
        for text, author in zip(texts, authors):
            self.append({
                'author': author,
                'text': text,
            })


urls = [
    'http://quotes.toscrape.com/page/{}/'.format(i) for i in range(1, 11)]


def get_quotes(n):
    pool = Pool(n)
    start = time.time()
    pool.map(QuoteMiner, urls)
    end = time.time()
    return end - start


for n in (1, 5, 10):
    print('{} thread(s): {}s'.format(n, get_quotes(n)))

# -*- coding: utf-8 -*-

from miner import Miner
from pony.orm import *

db = Database("sqlite", ":memory:", create_db=True)


class Quote(db.Entity):
    id = PrimaryKey(int, auto=True)
    author = Required(str)
    text = Required(str)


db.generate_mapping(create_tables=True)


@db_session
def save(data):
    Quote(**data)


class PonyQuote(Miner):
    def parse(self, dom):
        texts = dom.xpath('//div[@class="quote"]//span[@class="text"]/text()')
        authors = dom.xpath('//div[@class="quote"]//small/text()')
        for text, author in zip(texts, authors):
            save({
                'author': author,
                'text': text[1:-1],
            })


PonyQuote('http://quotes.toscrape.com/')
with db_session:
    quote_einstein = select(q.text for q in Quote if 'Einstein' in q.author)[:]
print(quote_einstein)

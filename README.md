# Miner

`Miner` is a very simple web crawler/scraper written in Python, inspired by [Sukhoi](https://github.com/iogf/sukhoi). It only requires [requests](http://docs.python-requests.org/en/master/) and [lxml](http://lxml.de/). It works under both python 2 and python 3.

# Usage

The simplest way to use `Miner` is to inherit it and override `Miner.parse`.

```python
from miner import Miner

class QuoteMiner(Miner):
    def parse(self, dom):
        texts = dom.xpath('//div[@class="quote"]//span[@class="text"]/text()')
        authors = dom.xpath('//div[@class="quote"]//small/text()')
        for text, author in zip(texts, authors):
            self.append({
                'author': author,
                'text': text[1:-1],
            })

url = 'http://quotes.toscrape.com/'
quotes = QuoteMiner(url)
```

# Examples

**quote.py:** Another `QuoteMiner`, only this time it also fetches information about authors.

**quote_thread.py:** Use thread to accelerate.

**quote_soup.py:** Use [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) instead of [lxml](http://lxml.de/).

**quote_pony.py:** Save to database, using [Pony ORM](https://ponyorm.com/).
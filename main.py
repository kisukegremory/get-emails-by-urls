import scrapy
from scrapy.crawler import CrawlerProcess
import re

regexEmail = re.compile(r"[\w\.-]+@[\w\.-]+\.\w+")
class QuoteSpider(scrapy.Spider):
    name = 'QuoteSpider'
    start_urls = [
        "https://sobreuol.noticias.uol.com.br/fale-com-uol/",
        "https://veja.abril.com.br/fale-conosco/"
    ]
    def parse(self, response):
        yield {
            'url':response.url,
            'emails':regexEmail.findall(response.text)
        }


if __name__ == "__main__":
  process = CrawlerProcess({
'FEED_FORMAT': 'json',
'FEED_URI': 'result.json'
})
  df = process.crawl(QuoteSpider)
  x = process.start()
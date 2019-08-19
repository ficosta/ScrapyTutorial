import scrapy


class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/'
    ]

    def parse(self, response):
        all_div_quotes = response.css('div.quote')
        title = all_div_quotes.css('span.text::text').extract()
        author = all_div_quotes.css('span.author::text').extract()
        tag = all_div_quotes.css('.tag::text').extract()
        yield {
            'titletext': title,
            'author': author,
            'tag': tag
        }

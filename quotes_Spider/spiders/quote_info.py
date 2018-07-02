# -*- coding: utf-8 -*-
import scrapy


class QuoteInfoSpider(scrapy.Spider):
    name = 'quote_info'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        quotes = response.xpath('//*[@class="quote"]')

        for quote in quotes:
            text = quote.xpath('.//*[@class="text"]/text()').extract_first()
            author = quote.xpath('.//*[@itemprop="author"]/text()').extract_first()
            tags = response.xpath('.//*[@itemprop="keywords"]/@content').extract_first()

            print('\n')
            print(text)
            print(author)
            print(tags)
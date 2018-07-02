# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com/']
    start_urls = ['http://quotes.toscrape.com']

    def parse(self, response):
        #Text in H1 tag
        h1 = response.xpath('//h1/a/text()').extract_first()
        #All tags text where class="tag-item"
        tags = response.xpath('//*[@class="tag-item"]/a/text()').extract()
        #key-value
        yield {'H1 Tag': h1, 'Tags': tags}
        #print(h1,tags)




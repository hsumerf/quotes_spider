# -*- coding: utf-8 -*-
import scrapy


class Quotes0Spider(scrapy.Spider):
    name = 'quotes0'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        pass

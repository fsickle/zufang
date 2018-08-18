# -*- coding: utf-8 -*-
import scrapy


class A58spiderSpider(scrapy.Spider):
    name = '58spider'
    allowed_domains = ['cd.58.com']
    start_urls = ['http://cd.58.com/']

    def parse(self, response):
        pass

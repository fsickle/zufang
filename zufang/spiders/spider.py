# -*- coding: utf-8 -*-
from scrapy import Spider, Request
from zufang.items import ZufangItem
import time
import random


class A58spiderSpider(Spider):
    name = 'spider'
    allowed_domains = ['cd.58.com']
    start_urls = ['http://cd.58.com/']
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75'
                      ' Safari/537.36',
        'Host': 'cd.58.com'
    }

    def start_requests(self):
        url = 'http://cd.58.com/chuzu/pn1/?PGTID=0d3090a7-0006-65e7-8302-226aa837f02e&ClickID=2'
        headers = self.headers.copy()
        yield Request(url, headers=headers, callback=self.parse_chuzu)

    def parse_chuzu(self, response):
        headers = self.headers.copy()
        next_page = response.xpath('//*[@id="bottom_ad_li"]/div[2]/a[@class="next"]/@href').extract_first()
        # print(next_page)
        item = ZufangItem()
        messages = response.xpath('/html/body/div[3]/div[1]/div[5]/div[2]/ul/li')[10:]
        for message in messages:
            try:
                item['href'] = message.xpath('./div[2]/h2/a/@href').extract_first()
            except:
                item['href'] = None
            try:
                item['describe'] = message.xpath('./div[2]/h2/a/text()').extract_first().strip()
            except:
                item['describe'] = None
            try:
                item['room'] = message.xpath('./div[2]/p[1]/text()').re_first('(.*?)\s')
            except:
                item['room'] = None
            try:
                location = message.xpath('./div[2]/p[2]/a').re('>(.*?)</a>')
                item['location'] = ' '.join(location)
            except:
                item['location'] = None
            try:
                item['price'] = message.xpath('./div[3]/div[2]/b/text()').extract_first()
            except:
                item['price'] = None
            yield item

        if next_page:
            time.sleep(30)
            yield Request(next_page, headers=headers, callback=self.parse_chuzu)







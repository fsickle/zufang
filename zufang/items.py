# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class ZufangItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    collection = 'tongcheng58'
    describe = Field()
    href = Field()
    room = Field()
    location = Field()
    price = Field()


# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GuidatraduzioniItem(scrapy.Item):
    # define the fields for your item here like:
    URL = scrapy.Field()
    VatNumber = scrapy.Field()
    Are = scrapy.Field()
    FirstFreeTranslation = scrapy.Field()
    MajorCustomers = scrapy.Field()
    StaffConsistOf = scrapy.Field()
    Languages = scrapy.Field()
    OfficialTranslators = scrapy.Field()
    TransWebPages = scrapy.Field()
    AvgPriceTrans = scrapy.Field()
    Descriptions = scrapy.Field()


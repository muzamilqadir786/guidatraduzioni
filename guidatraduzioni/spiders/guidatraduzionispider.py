# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from guidatraduzioni.items import GuidatraduzioniItem
from scrapy.http import Request
import urllib2
from lxml.html import fromstring
from scrapy.contrib.spiders import Rule
from scrapy.contrib.linkextractors import LinkExtractor

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import string

class GuidatraduzionispiderSpider(scrapy.Spider):
    name = "guidatraduzionispider"
    allowed_domains = ["http://www.guidatraduzioni.it"]
    start_urls = ['http://www.guidatraduzioni.it/imprese.html']

    def parse(self, response):
    	print "herereere"
    	print self.start_urls
    	for x in xrange(2,96):
    		link = 'http://www.guidatraduzioni.it/imprese_{}.html'.format(x) 
    		print link    		
    		yield Request(link,self.parse_links,dont_filter=True)
    def parse_links(self,response):
    	hxs = Selector(response)
    	links = hxs.xpath('//a[@class="fn com_name org jq_company_card"]/@href').extract()
    	for link in list(set(links)):
    		yield Request('http://www.guidatraduzioni.it'+link,self.parse_item,dont_filter=True)

    def parse_item(self,response):
    	hxs = Selector(response)
    	print "here in parse item"    	
    	item = GuidatraduzioniItem()
    	print response.url
    	item["URL"] = response.url
    	vat_no = hxs.xpath('//div[@class="adv-element"][1]/ul/li/text()').extract()    	
    	print vat_no
    	if vat_no:
    		item["VatNumber"] = vat_no[0].strip()
    	are = hxs.xpath('//div[@class="adv-element"][2]/ul/li/text()').extract()
    	if are:
    		item["Are"] = are[0]
    		print are

    	first_free_translation = hxs.xpath('//div[@class="adv-element"][3]/ul/li/text()').extract()
    	if first_free_translation:
    		item["FirstFreeTranslation"] = first_free_translation[0]
    		print first_free_translation

    	major_customers = hxs.xpath('//div[@class="adv-element"][4]/ul/li/text()').extract()
    	if major_customers:
    		item["MajorCustomers"] = major_customers
    		print major_customers

		
		staff_consist_of = hxs.xpath('//div[@class="adv-element"][5]/ul/li/text()').extract()
		if staff_consist_of:
			item["StaffConsistOf"] = staff_consist_of
    		print staff_consist_of

    	languages = hxs.xpath('//div[@class="adv-element"][6]/ul/li/text()').extract()
    	if languages:
    		item["Languages"] = languages
    		print languages

    	official_translators = hxs.xpath('//div[@class="adv-element"][7]/ul/li/text()').extract()
    	if official_translators:
    		item["OfficialTranslators"] = official_translators
    		print official_translators

    	trans_web_pages = hxs.xpath('//div[@class="adv-element"][8]/ul/li/text()').extract()
    	if trans_web_pages:
    		item["TransWebPages"] = trans_web_pages[0].decode("utf-8")
    		print trans_web_pages

    	
    	avg_price_trans = hxs.xpath('//div[@class="adv-element"][9]/ul/li/text()').extract()
    	if avg_price_trans:
    		item["AvgPriceTrans"] = avg_price_trans
    		print avg_price_trans

    	descriptions = hxs.xpath('//div[@class="company-description"]//text()').extract()
    	if descriptions:    		
    		descriptions = filter(lambda word:"\n" not in word,descriptions)
    		exclude = set(string.punctuation)
    		item["Descriptions"] = ''.join([ch for ch in descriptions if ch not in exclude])
    		print descriptions
    	


   		#print item 		
    	yield item
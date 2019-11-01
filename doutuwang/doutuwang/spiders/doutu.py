# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class DoutuSpider(CrawlSpider):
    name = 'doutu'
    allowed_domains = ['doutula.com']
    start_urls = ['http://www.doutula.com/']

    rules = (
        # Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'http://www.doutula.com/article/detail/\d+'), callback='parse_item', follow=False)

    )

    def parse_item(self, response):
        # item = {}
        img_urls = response.xpath('.//div[@class="pic-content"]//img/@src').extract()
        print(len(img_urls),response.url)
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        # return item

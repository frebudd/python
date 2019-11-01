# -*- coding: utf-8 -*-
import scrapy


class BaidutiebaSpider(scrapy.Spider):
    name = 'baidutieba'
    allowed_domains = ['https://tieba.baidu.com/p/6045832676?see_lz=1']
    start_urls = ['http://https://tieba.baidu.com/p/6045832676?see_lz=1/']

    def parse(self, response):
        pass

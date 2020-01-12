# -*- coding: utf-8 -*-
import scrapy
from EnergyParser.items import EnergyparserItem

ZIPCODE = '52001'
class EnergySpider(scrapy.Spider):
    name = 'energy'
    # allowed_domains = ['https://www.ree.es/en/balance-diario/peninsula/2014/01/01/d']
    start_urls = ['https://www.ree.es/en/balance-diario/peninsula/2014/01/01/d/']
    url_template = 'https://www.ree.es/en/balance-diario/peninsula/2014/{:02d}/{:02d}/d/'
    D = 1
    M = 1

    # set custom settings
    custom_settings = {
        'DEPTH_LIMIT': 3,
        'FEED_URI': 'energy_peninsula.csv'
    }


    def parse(self, response):
        for m in range(1, 13):
            for d in range(1, 32):
                NextUrl = self.url_template.format(m, d)
                print(NextUrl, self.D)
                yield response.follow(NextUrl, callback=self.parse_data)


    def parse_data(self, response):
        info = EnergyparserItem()
        info['date'] = response.xpath('//tr[@class="primera"]/th[1]/text()').extract()
        info['demand_bc'] = response.xpath('//tr[@class="datos demandasup even"]/td[1]/text()').extract()
        yield info

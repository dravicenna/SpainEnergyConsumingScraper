# -*- coding: utf-8 -*-
import scrapy
from EnergyParser.items import EnergyparserItem

class MelillaSpider(scrapy.Spider):
    name = 'melilla'
    # Start URL
    start_urls = ['https://www.ree.es/en/balance-diario/melilla/2014/01/01/']

    url_template = 'https://www.ree.es/en/balance-diario/melilla/20{}/{:02d}/{:02d}/'

    # set custom settings
    custom_settings = {
        # 'DEPTH_LIMIT': 2,
        'FEED_FORMAT': "csv", # Save format
        'FEED_URI': 'energy_melilla.csv' # File name
    }


    def parse(self, response):
        '''
        Function for crawling
        '''
        for year in range(14, 20): # From 2014 to 2019
            for month in range(1, 13): # From Jun to Dec
                for day in range(1, 32): # Days from 1 to 31
                    NextUrl = self.url_template.format(year, month, day)
                    yield response.follow(NextUrl, callback=self.parse_data)


    def parse_data(self, response):
        '''
        Function for scraping
        '''
        info = EnergyparserItem()
        info['date'] = response.url.split("/")[6:9]
        info['Diesel_engines'] = response.xpath('//table[1]/tbody[1]/tr[2]/td[1]/text()').extract()
        info['Gas_turbine'] = response.xpath('//table[1]/tbody[1]/tr[3]/td[1]/text()').extract()
        info['Fuel_oil_gas'] = response.xpath('//table[1]/tbody[1]/tr[4]/td[1]/text()').extract()
        info['Solar_PV'] = response.xpath('//table[1]/tbody[1]/tr[5]/td[1]/text()').extract()
        info['Non_renewable_waste'] = response.xpath('//table[1]/tbody[1]/tr[6]/td[1]/text()').extract()
        info['Renewable_waste'] = response.xpath('//table[1]/tbody[1]/tr[7]/td[1]/text()').extract()
        info['Generation'] = response.xpath('//table[1]/tbody[1]/tr[8]/td[1]/text()').extract()
        info['Demand'] = response.xpath('//table[1]/tbody[1]/tr[9]/td[1]/text()').extract()
        info['Peak_Load'] = response.xpath('//table[2]/tbody[1]/tr[2]/td[1]/text()').extract()
        info['Daily_demand'] = response.xpath('//table[2]/tbody[1]/tr[3]/td[1]/text()').extract()

        yield info
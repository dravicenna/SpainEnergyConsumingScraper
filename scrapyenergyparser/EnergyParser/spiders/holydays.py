# -*- coding: utf-8 -*-
import scrapy
import re
from EnergyParser.items import MelillaHolydayItem

class HolydaysSpider(scrapy.Spider):
    name = 'holydays'
    start_urls = ['https://www.officeholidays.com/countries/spain/melilla/2015']
    url_template = 'https://www.officeholidays.com/countries/spain/melilla/20{}'

    # set custom settings
    custom_settings = {
        'FEED_FORMAT': "csv",
        'FEED_URI': 'holyday_melilla.csv'
    }
    def parse(self, response):
        """
        Enumerate pages from 2015 to 2019
        """
        for Y in range(14, 20):
            NextUrl = self.url_template.format(Y)
            yield response.follow(NextUrl, callback=self.parse_data)

    def parse_data(self, response):
        """
        Parse every page
        """
        info = MelillaHolydayItem()
        date = response.xpath('//time[@itemprop="startDate"]/@datetime').extract()
        type = response.xpath('//td[@class="comments"]/text()').extract()
        name = response.xpath('//a[@class="country-listing"]/text()').extract()

        for i in range(len(date)):
            info['type'] = type[i]
            info['name'] = name[i]
            info['date'] = date[i]
            yield info


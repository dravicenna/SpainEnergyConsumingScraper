# -*- coding: utf-8 -*-
import scrapy
import re
import json
from EnergyParser.items import WeatherparserItem

class WeatherMelillaSpider(scrapy.Spider):
    name = 'weather_melilla'
    # allowed_domains = ['www.timeanddate.com/weather/spain/melilla/historic?month=1']
    # start_urls = ['https://www.timeanddate.com/weather/spain/melilla/historic?month=1&year=2014']
    start_urls = ['https://www.timeanddate.com/weather/spain/melilla/historic?hd=20140101']
    url_template = 'https://www.timeanddate.com/weather/spain/melilla/historic?month={}&year=20{}'

    # set custom settings
    custom_settings = {
        'DEPTH_LIMIT': 2,
        'FEED_FORMAT': "csv",
        'FEED_URI': 'weather_melilla.csv'
    }

    # "detail": (.+?)\, \"grid\"
    def parse(self, response):

        for Y in range(14, 20):
            for M in range(1, 13):
                NextUrl = self.url_template.format(M, Y)
                # print(NextUrl)
                yield response.follow(NextUrl, callback=self.parse_data)


    def parse_data(self, response):
        info = WeatherMelillaSpider()
        raw_data = re.findall(r'"detail":(.+?)\,\"grid\"', response.body.decode("utf-8"))[0]
        data_json = json.loads(raw_data)
        # print(type(data_json))
        # print(type(data_json[0]))
        # print('PRINT', data_json[0]['hls'])
        # print('PRINT2', data_json[0])
        for x in range(len(data_json)):
            yield data_json[x]



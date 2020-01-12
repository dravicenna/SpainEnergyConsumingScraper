# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class EnergyparserItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    date = scrapy.Field()
    Diesel_engines = scrapy.Field()
    Gas_turbine = scrapy.Field()
    Fuel_oil_gas = scrapy.Field()
    Solar_PV = scrapy.Field()
    Non_renewable_waste = scrapy.Field()
    Renewable_waste = scrapy.Field()
    Generation = scrapy.Field()
    Demand = scrapy.Field()
    Peak_Load = scrapy.Field()
    Daily_demand = scrapy.Field()
    pass


class WeatherparserItem(scrapy.Item):
    date = scrapy.Field()

    pass


class MelillaHolydayItem(scrapy.Item):
    # define the fields for your item here like:
    # year = scrapy.Field()
    date = scrapy.Field()
    type = scrapy.Field()
    name = scrapy.Field()
    pass
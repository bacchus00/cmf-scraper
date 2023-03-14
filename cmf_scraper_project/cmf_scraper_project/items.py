# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CmfScraperProjectItem(scrapy.Item):
    # define the fields for your item here like:
    company_name = scrapy.Field()
    company_rut = scrapy.Field()
    director_rut = scrapy.Field()
    director_name = scrapy.Field()
    director_position = scrapy.Field()
    director_appointment_date = scrapy.Field()

    pass

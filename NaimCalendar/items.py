# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CalendarItem(scrapy.Item):
    lesson = scrapy.Field()
    teacher = scrapy.Field()
    location = scrapy.Field()
    start_time = scrapy.Field()
    end_time = scrapy.Field()
    date = scrapy.Field()

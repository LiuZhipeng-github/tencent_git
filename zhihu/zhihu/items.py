# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhihuItem(scrapy.Item):
    author = scrapy.Field()
    comment_time = scrapy.Field()
    comment = scrapy.Field()
    gender = scrapy.Field()

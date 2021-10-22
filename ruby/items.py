# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class Province(Item):
    table = 'jewel_province'
    id = Field()
    provinceName = Field()
    initial = Field()

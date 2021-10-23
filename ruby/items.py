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


class House(Item):
    table = 'jewel_house'
    id = Field()
    title = Field()
    price = Field()
    layout = Field()
    area = Field()
    uni_price = Field()
    floor = Field()
    orientations = Field()
    houseType = Field()
    remodel = Field()
    year = Field()
    village = Field()
    address = Field()
    url = Field()


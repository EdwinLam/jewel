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


class IpProxy(Item):
    # define the fields for your item here like:
    table = 'jewel_proxy_ip'
    id = Field()
    ip = Field()
    port = Field()
    # 匿名度
    anons = Field()
    # 类型：http/https
    schema = Field()
    # 国家
    country = Field()
    country_img = Field()
    province = Field()
    isp = Field()
    # 位置
    position = Field()
    # 响应速度
    speed = Field()
    # 最后验证时间
    verify_time = Field()

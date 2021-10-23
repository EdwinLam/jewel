# -*- coding: utf-8 -*-
import scrapy
from execjs import execjs
import sys
import json
from ruby.util.Snowflake import IdWorker
import re

from lxml import etree
from ruby.items import Province, House


class FiftyEight(scrapy.Spider):
    name = "58"

    def start_requests(self):
        yield scrapy.Request(url="https://zs.58.com/ershoufang", callback=self.parse_house)

    def parse(self, response):
        data = response.css('script::text')
        ctx = execjs.compile(data[0].get())
        provinces = ctx.eval('provinceList')
        for provinceName in provinces:
            item = Province()
            item['provinceName'] = provinceName
            item['initial'] = provinces[provinceName]
            item['id'] = 1

            self.logger.debug(item)
            yield item

    def parse_house(self, response):
        res = response.css('.list .property')
        for el in res:
            print('==========')
            item = House()
            title = el.css('.property-content-title h3::text').get()
            line = re.split('\s+', title)  # 将字符串i以全部空白字符为分割符，将其分割成一个字符列表
            new_line = ','.join(line)  # 将字符列表用','拼接成一个新字符串
            title = new_line.strip(',')  # 将新字符串尾部产生的','
            item['title'] = title
            layout_el = el.css('.property-content-info-text.property-content-info-attribute')
            tmp = etree.HTML(text=layout_el.get())
            layout = tmp.xpath('string(.)').replace(' ', '')
            item['layout'] = layout
            item['price'] = el.css('.property-price-total-num::text').get() + el.css(
                '.property-price-total-text::text').get()
            item['uni_price'] = el.css('.property-price-average::text').get()
            for info in el.css('.property-content-info-text::text'):
                self.auto_set_items(item, info.get().replace(' ', '').replace('\n', ''))
            address_el = el.css('.property-content-info-comm-address')
            tmp = etree.HTML(text=address_el.get())
            address = tmp.xpath('string(.)').replace(' ', '')
            item['address'] = address
            item['village'] = el.css('.property-content-info-comm-name::text').get()
            print(item)

    def auto_set_items(self, item, value):
        if '年' in value:
            item['year'] = value
        if '层' in value:
            item['floor'] = value
        if '㎡' in value:
            item['area'] = value
        if any(f in value for f in ['东', '南', '西', '北']):
            item['orientations'] = value

    def parse_house_info(self, el):
        tmp = etree.HTML(text=el.get())
        return tmp.xpath('string(.)')

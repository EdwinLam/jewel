# -*- coding: utf-8 -*-
import scrapy
from execjs import execjs
import sys
import json
from ruby.util.Snowflake import IdWorker
from ruby.items import Province


class FiftyEight(scrapy.Spider):
    name = "58"

    def start_requests(self):
        yield scrapy.Request(url="https://www.58.com/changecity.html?fullpath=0", callback=self.parse)

    def parse(self, response):
        data = response.css('script::text')
        ctx = execjs.compile(data[0].get())
        provinces = ctx.eval('provinceList')
        for provinceName in provinces:
            worker = IdWorker(1, 2, 0)
            item = Province()
            item['provinceName'] = provinceName
            item['initial'] = provinces[provinceName]
            item['id'] = 1

            self.logger.debug(item)
            yield item

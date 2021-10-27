# -*- coding: utf-8 -*-
import scrapy
import urllib3
from ruby.items import IpProxy
from PIL import Image
from io import BytesIO
import pytesseract
import requests
from urllib.parse import urlparse


class ProxyIp(scrapy.Spider):
    name = "proxy_ip"

    def start_requests(self):
        url_list = [
            'https://proxy.mimvp.com/freeopen',
            'https://proxy.mimvp.com/freeopen?proxy=in_tp'
        ]
        for url in url_list:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        domain = response.url
        for el in response.css('.free-proxylist-tbl tbody tr'):
            item = IpProxy()
            item['ip'] = el.css('.free-proxylist-tbl-proxy-ip::text').get()
            item['schema'] = el.css('.free-proxylist-tbl-proxy-type::text').get()
            item['anons'] = el.css('.free-proxylist-tbl-proxy-anonymous::text').get()
            item['country_img'] = el.css('.free-proxylist-tbl-proxy-country img::attr(src)').get()
            item['country'] = el.css('.free-proxylist-tbl-proxy-country::text').get().replace(' (', ' ').strip()
            province = el.css('.free-proxylist-tbl-proxy-country font::text').get().strip()
            item['province'] = '' if province == 'null' else province
            item['port'] = self.get_port(domain, el)
            item['isp'] = el.css('.free-proxylist-tbl-proxy-isp::text').get()
            print(item)

    @staticmethod
    def get_port(domain, el):
        img_path = el.css('.free-proxylist-tbl-proxy-port img::attr(src)').get()
        url_res = urlparse(domain)
        img_url = url_res.scheme + '://' + url_res.netloc + img_path
        res = requests.get(img_url)
        image = Image.open(BytesIO(res.content))
        return pytesseract.image_to_string(image, config='outputbase digits').strip()

from ruby.spiders.proxy.source import IBaseProxySource
import scrapy


class MimvpSource(IBaseProxySource):
    url_list = [
        'https://proxy.mimvp.com/freeopen',
        'https://proxy.mimvp.com/freeopen?proxy=in_tp'
    ]

    @staticmethod
    def fetch_proxy_ip(self):
        for url in self.url_list:
            yield scrapy.Request(url=url, callback=self.parse)

    @staticmethod
    def parse(self, response):
        print(response)

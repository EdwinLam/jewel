from abc import ABC, abstractmethod


class IBaseProxySource(ABC):
    @staticmethod
    @abstractmethod
    def fetch_proxy_ip(self):
        pass

    @staticmethod
    @abstractmethod
    def parse(self, response):
        pass

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


class ZhihuSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class ZhihuDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
class CookiesMiddleware(object):
    """ 维护Cookie """

    def __init__(self):
        self.cookie_tem = [
            '_zap=9514d242-5fb2-4972-9f6d-ec706dad0abb; d_c0="ALDSV4pufRGPTi3lfG2pdcXrb2oUvPUL6N8=|1593255361"; _ga=GA1.2.1278649368.1593255365; _xsrf=iwf4I2cdGaKKNx2NW5Ym6CIRi7wl8P2F; z_c0="2|1:0|10:1598942355|4:z_c0|92:Mi4xNnJ6QUF3QUFBQUFBc05KWGltNTlFU1lBQUFCZ0FsVk5rem83WUFDNExHWk9RbGpmSW1WaFlGNWpkR2QxUTl0Xy1B|91fc3b8f632a42eceb8f1a13e83db8b4cafc718b81aede3828e87649900eb4df"; tst=r; q_c1=02da1dd2bf0f4fa3823b4ea60e709079|1609416247000|1598100799000; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1610595168,1610624644,1611105368,1611112062; SESSIONID=79EdaTReeDPE9ek2plqOd0OzavxsIjVEW9tkum38nGW; JOID=WlsVBUv8nOyCtgfTRPL_v6V8nlNdwKav4N9YgieR07_BiWqzdXQH6-y1D9ZEZUVvahZVlXmqDUBWrHOXOKHtjd8=; osd=W1AUAk79l-2FswbYRfX6vq59mVZcy6eo5d5TgyCU0rTAjm-yfnUA7u2-DtFBZE5ubRNUnnitCEFdrXSSOarsito=; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1611112101; KLBRSID=81978cf28cf03c58e07f705c156aa833|1611112102|1611112059',
        ]

    def process_request(self, request, spider):
        request.cookies = {'cookie': self.cookie_tem[0]}

    def process_response(self, request, response, spider):
        if response.status in [300, 301, 302, 303]:
            print('需要重定向')
            return response
        elif response.status in [403, 414, 404]:
            print('cookie已失效')
            return response
        else:
            # print('cookie可以使用')
            return response
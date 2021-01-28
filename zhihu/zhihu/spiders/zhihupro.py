import json
import re
import time

import scrapy
from scrapy_redis.spiders import RedisSpider
# -----1导入分布式爬虫类
from zhihu.items import ZhihuItem


class ZhihuSpider(RedisSpider):  # ----2 继承RedisSpider类方法
    name = 'zhihupro'
    # ----4 设置redis-key
    redis_key = 'zhihu:start_urls'

    # ----5 设置__init__
    def __init__(self, *args, **kwargs):
        domain = kwargs.pop('domain', '')
        self.allowed_domains = list(filter(None, domain.split(',')))
        super(ZhihuSpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        first_layer = json.loads(response.text)
        is_end = first_layer['paging']['is_end']
        next_url = first_layer['paging']['next']
        for data in first_layer['data']:
            author_id = data['target']['id']
            type_comment = data['target']['type']
            if data['target']['comment_count'] != 0:
                url = f"https://www.zhihu.com/api/v4/{type_comment}s/{author_id}/root_comments?order=normal&limit=20&offset=0&status=open"
                yield scrapy.Request(url, callback=self.parse_comment)

        if not is_end:
            yield scrapy.Request(next_url, callback=self.parse)

    def parse_comment(self, response):
        # response.encoding = ('utf-8')
        second_layer = json.loads(response.text)
        gender_dic = {'1': '男', '-1': '匿名', '0': '女'}
        is_end = second_layer['paging']['is_end']
        next_url = second_layer['paging']['next']
        for data in second_layer['data']:
            if '<p>' in data['content']:
                data['content'] = re.findall('<p>(.+?)</p>', data['content'])[0]
            comment_item = ZhihuItem()
            comment_item['author'] = data['id']
            comment_item['comment'] = data['content']
            comment_item['comment_time'] = time.strftime('%Y%m%d%H%S', time.gmtime(data['created_time']))
            comment_item['gender'] = gender_dic[str(data['author']['member']['gender'])]

            yield comment_item
        if not is_end:
            yield scrapy.Request(next_url, callback=self.rest_comment)

    def rest_comment(self, response):
        gender_dic = {'1': '男', '-1': '匿名', '0': '女'}
        # response.encoding = ('utf-8')
        second_layer = json.loads(response.text)
        is_end = second_layer['paging']['is_end']
        next_url = second_layer['paging']['next']
        for data in second_layer['data']:
            if '<p>' in data['content']:
                data['content'] = re.findall('<p>(.+?)</p>', data['content'])[0]
            comment_item = ZhihuItem()
            comment_item['author'] = data['id']
            comment_item['comment'] = data['content']
            comment_item['comment_time'] = time.strftime('%Y%m%d%H%S', time.gmtime(data['created_time']))
            comment_item['gender'] = gender_dic[str(data['author']['member']['gender'])]
            # print(data['content'], '33333333333333')
            yield comment_item
        if not is_end:
            yield scrapy.Request(next_url, callback=self.rest_comment)

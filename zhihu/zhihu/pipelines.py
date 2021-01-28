# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exporters import CsvItemExporter

class ZhihuPipeline:
    def __init__(self):
        self.file = open("data_zhihu.csv", "wb")
        self.exporter = CsvItemExporter(self.file, encoding='utf-8')
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()
        print('+++++++++++++++++++++++++++++++++')

    def process_item(self, item, spider):
        self.exporter.export_item(dict(item))
        print('--------------------------------')
        return item
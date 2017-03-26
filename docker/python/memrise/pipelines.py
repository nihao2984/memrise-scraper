import csv

from scrapy import signals
from scrapy.contrib.exporter import CsvItemExporter


class CSVPipeline(object):

    def __init__(self):
        self.files = {}
        self.items = []

    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline

    def spider_opened(self, spider):
        file = open('/opt/memrise_{}.csv'.format(spider.name), 'w+b')
        self.files[spider] = file
        self.exporter = CsvItemExporter(file)
        self.exporter.fields_to_export = [
            'polish',
            'english',
            'example',
            'grammatical_type',
        ]
        self.exporter.start_exporting()

    def spider_closed(self, spider):
        items = sorted(self.items, key=lambda i: i['polish'])
        for item in items:
            self.exporter.export_item(item)

        self.exporter.finish_exporting()
        file = self.files.pop(spider)
        file.close()

    def process_item(self, item, spider):
        self.items.append(item)
        return item

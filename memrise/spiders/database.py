import scrapy

from memrise.items import DatabaseItem


class MemriseDatabaseSpider(scrapy.Spider):
    name = 'database'

    def start_requests(self):
        return [scrapy.Request(
            url='http://www.memrise.com/course/1049040/mikes-polish-vocabulary/edit/database/2014145/?page={}'.format(page),
            cookies={
                'sessionid': self.settings.get('MEMRISE_SESSION_ID'),
            },
            callback=self.process_page
        ) for page in range(1, self.settings.getint('MEMRISE_PAGE_COUNT') + 1)]

    def process_page(self, response):
        f = lambda t, i: t.css('td:nth-child({}) div.text::text'.format(i)).extract()
        for thing in response.css('tr.thing'):
            item = DatabaseItem()
            item['polish'] = f(thing, 2)
            item['english'] = f(thing, 3)
            item['example'] = f(thing, 4)
            item['grammatical_type'] = f(thing, 5)
            yield item

import scrapy

from memrise.items import LevelItem


class MemriseLevelsSpider(scrapy.Spider):
    name = 'levels'

    def start_requests(self):
        return [scrapy.Request(
            url='http://www.memrise.com/course/{}/{}/{}/'.format(
                self.settings.get('MEMRISE_COURSE_ID'),
                self.settings.get('MEMRISE_COURSE_NAME'),
                level
            ),
            callback=self.process_level
        ) for level in range(1, self.settings.getint('MEMRISE_LEVEL_COUNT') + 1)]

    def process_level(self, response):
        f = lambda t, c: t.css('div.col_{} div.text::text'.format(c)).extract()
        for thing in response.css('div.thing.text-text'):
            item = LevelItem()
            item['polish'] = f(thing, 'a')
            item['english'] = f(thing, 'b')
            yield item

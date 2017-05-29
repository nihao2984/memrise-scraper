import scrapy

from memrise.items import LevelItem


class MemriseLevelsSpider(scrapy.Spider):
    name = 'levels'

    def start_requests(self):
        return [scrapy.Request(
            url='{}/course/{}/{}/{}/'.format(
                self.settings.get('MEMRISE_BASE_URL'),
                self.settings.get('MEMRISE_COURSE_ID'),
                self.settings.get('MEMRISE_COURSE_NAME'),
                level
            ),
            callback=self.process_level
        ) for level in range(
            self.settings.getint('MEMRISE_MIN_LEVEL'),
            self.settings.getint('MEMRISE_MAX_LEVEL') + 1
        )]

    def process_level(self, response):
        def f(t, c):
            return t.css('div.col_{} div.text::text'.format(c)).extract()

        for thing in response.css('div.thing.text-text'):
            item = LevelItem()
            item['polish'] = f(thing, 'a')
            item['english'] = f(thing, 'b')
            yield item

import scrapy

level_count = 8


class MemriseLevelSpider(scrapy.Spider):
    name = 'Memrise level spider'

    def start_requests(self):
        return [scrapy.Request(
            url='http://www.memrise.com/course/1049040/mikes-polish-vocabulary/{}/'.format(level),
            callback=self.process_level
        ) for level in range(1, level_count + 1)]

    def process_level(self, response):
        f = lambda t, c: t.css('div.col_{} div.text::text'.format(c)).extract()
        for thing in response.css('div.thing.text-text'):
            yield {
                'polish': f(thing, 'a'),
                'english': f(thing, 'b'),
            }

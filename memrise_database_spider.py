import scrapy

page_count = 51
sessionid = 'top-secret'


class MemriseDatabaseSpider(scrapy.Spider):
    name = 'Memrise database spider'

    def start_requests(self):
        return [scrapy.Request(
            url='http://www.memrise.com/course/1049040/mikes-polish-vocabulary/edit/database/2014145/?page={}'.format(page),
            cookies={
                'sessionid': sessionid,
            },
            callback=self.process_page
        ) for page in range(1, page_count + 1)]

    def process_page(self, response):
        f = lambda t, i: t.css('td:nth-child({}) div.text::text'.format(i)).extract()
        for thing in response.css('tr.thing'):
            yield {
                'polish': f(thing, 2),
                'english': f(thing, 3),
                'example': f(thing, 4),
                'type': f(thing, 5),
            }

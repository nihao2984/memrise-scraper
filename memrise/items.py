import scrapy


class LevelItem(scrapy.Item):
    polish = scrapy.Field()
    english = scrapy.Field()


class DatabaseItem(LevelItem):
    example = scrapy.Field()
    grammatical_type = scrapy.Field()

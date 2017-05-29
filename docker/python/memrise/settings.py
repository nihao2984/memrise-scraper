SPIDER_MODULES = [
    'memrise.spiders',
]

ITEM_PIPELINES = {
    'memrise.pipelines.CSVPipeline': 100,
}

MEMRISE_BASE_URL = 'https://www.memrise.com'

MEMRISE_COURSE_ID = '1049040'

MEMRISE_DATABASE_ID = '2014145'

MEMRISE_COURSE_NAME = 'mikes-polish-course'

MEMRISE_MIN_LEVEL = 1

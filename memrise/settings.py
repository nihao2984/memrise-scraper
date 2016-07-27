SPIDER_MODULES = [
    'memrise.spiders',
]

ITEM_PIPELINES = {
    'memrise.pipelines.CSVPipeline': 100,
}

MEMRISE_COURSE_ID = '1049040'

MEMRISE_DATABASE_ID = '2014145'

MEMRISE_COURSE_NAME = 'mikes-polish-course'

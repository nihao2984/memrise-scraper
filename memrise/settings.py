SPIDER_MODULES = [
    'memrise.spiders',
]

ITEM_PIPELINES = {
    'memrise.pipelines.CSVPipeline': 100,
}

MEMRISE_PAGE_COUNT = 62

MEMRISE_LEVEL_COUNT = 9

MEMRISE_SESSION_ID = 'top-secret'

SPIDER_MODULES = [
    'memrise.spiders',
]

ITEM_PIPELINES = {
    'memrise.pipelines.CSVPipeline': 100,
}

MEMRISE_PAGE_COUNT = 69

MEMRISE_LEVEL_COUNT = 12

MEMRISE_SESSION_ID = 'top-secret'

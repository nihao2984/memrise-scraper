#!/bin/bash

docker-compose run --rm python scrapy crawl levels -s MEMRISE_MIN_LEVEL=1 -s MEMRISE_MAX_LEVEL=$1
docker-compose run --rm python scrapy crawl database -s MEMRISE_SESSION_ID=$2 -s MEMRISE_PAGE_COUNT=$3

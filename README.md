# Memrise scraper

* `vagrant up`
* Get the session cookie off the `memrise.com` after having logged in
* Put the session cookie in `memrise_database_spider.py`
* Put the number of databaes pages (at the time of writing, 20 items per page) in `memrise_database_spider.py`
* Run `scrapy runspider memrise_database_spider.py -o memrise_spider.csv`

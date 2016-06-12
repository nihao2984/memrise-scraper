# Memrise scraper

* `vagrant up`
* Get the session cookie off the `memrise.com` after having logged in
* Put the session cookie in `memrise_database_spider.py`
* Put the number of databases pages in `memrise_database_spider.py`
* Run `scrapy runspider memrise_database_spider.py -o memrise_spider.csv`

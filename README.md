# Memrise scraper

* Get the session cookie off `memrise.com` after having logged in
* Put the session cookie in `memrise_database_spider.py`
* Put the number of databases pages in `memrise_database_spider.py`
* Put the number of levels in `memrise_levels_spider.py`

```
vagrant up
vagrant ssh
workon py2
scrapy runspider memrise_database_spider.py -o memrise_database.csv
scrapy runspider memrise_levels_spider.py -o memrise_levels.csv
```

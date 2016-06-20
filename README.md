# Memrise scraper

* Get the session cookie off `memrise.com` after having logged in
* Put the session cookie in `memrise/settings.py`
* Put the number of databases pages in `memrise/settings.py`
* Put the number of levels in `memrise/settings.py`

```
vagrant up
vagrant ssh
workon py2
scrapy crawl database
scrapy crawl levels
```

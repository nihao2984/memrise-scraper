# Memrise scraper

## General

Specify properties of the course to be crawled in `memrise/settings.py`:

```
MEMRISE_COURSE_ID   = '1049040'
MEMRISE_DATABASE_ID = '2014145'
MEMRISE_COURSE_NAME = 'mikes-polish-course'
```

Then run:

```
vagrant up
vagrant ssh
workon py2
```

## Levels

Specify the number of levels in the course, then run:

```
scrapy crawl levels -s MEMRISE_LEVEL_COUNT=123
```

## Database

Specify the session cookie (which can be taken from `memrise.com` while logged in).

Specify the number of database pages (from the database editor in the course), then run:

```
scrapy crawl database -s MEMRISE_SESSION_ID='top-secret' -s MEMRISE_PAGE_COUNT=123
```

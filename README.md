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
scrape a b c
```

Where:

* `a` is the number of levels in the course
* `b` is the session cookie (i.e. must be logged in)
* `c` is the number of database pages (in the course editor)

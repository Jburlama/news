This Python script locates articles worldwide, orders them by popularity using the NewsAPI, and stores them in an SQLite database.

In the command line, you have the option to set:

q: topic of the article

day: the date the article was published

limit: number of articles to fetch


Usage:

`python3 main.py` default q=technology day=today limit=100

`python3 main.py q=topic day=yyyy-mm-dd limit=[1-100]`

Requirement:

```pip install requests```


# DEMO

https://github.com/user-attachments/assets/4999a6ea-8bf2-4b34-9e81-8c3fa28793b2


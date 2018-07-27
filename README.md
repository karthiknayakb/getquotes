# getquotes
scrapes quotes from famousquotesandauthors site

Steps:
1. create a folder quotes
2. run python getquotecategory.py
3. run python getquotes.py
4. run python combileall.py if you want all quotes in one file (./quotes/combinedAll.json).

All quotes are downloaded in quotes folder in json format.

Use "getquotesparallel.py" instead of "getquotes.py" for parallel execution. It is faster but Resource intensive!
This was tested on ubuntu. Cannot guarantee on other environments.

Dependencies:
1. Python 2.7
2. urllib2
3. bs4

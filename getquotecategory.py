import urllib2
from bs4 import BeautifulSoup

link = "http://www.famousquotesandauthors.com/quotes_by_topic.html"

page = urllib2.urlopen(link)
soup = BeautifulSoup(page,"lxml")
quotesArray = soup.findAll("table")
col1 = quotesArray[14]
col2 = quotesArray[15]
col3 = quotesArray[16]

c1data = col1.findAll("a")
c2data = col2.findAll("a")
c3data = col3.findAll("a")
linkarray = []
for i in c1data:
	linkarray.append(["http://www.famousquotesandauthors.com"+str(i['href'])])

for i in c2data:
	linkarray.append(["http://www.famousquotesandauthors.com"+str(i['href'])])

for i in c3data:
	linkarray.append(["http://www.famousquotesandauthors.com"+str(i['href'])])

with open("categories.csv",'w') as f:
	for l in linkarray:
		for m in l:
			f.write(m)
		f.write('\n')
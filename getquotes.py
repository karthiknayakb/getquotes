import urllib2
from bs4 import BeautifulSoup
import json
import csv

#link = "http://www.famousquotesandauthors.com/topics/acting_quotes.html"


def getquotes(link):
	page = urllib2.urlopen(link)
	soup = BeautifulSoup(page,"lxml")
	quotesArray = soup.findAll("td")

	quotes = quotesArray[-35:-34:]

	quotes = quotes[0].findAll("div")
	quotedic = []
	x,y=2,4
	title = str(quotes[0].getText().replace(" Quotes and Quotations",""))
	while y<len(quotes):
		quotedic.append({"quote":str(quotes[x:y][0].getText()),"name":str(quotes[x:y][1].getText()).strip().replace("-","").strip()})
		x+=4
		y+=4
	outfile = open("quotes/"+title+".json","w")
	json.dump(quotedic,outfile)
	outfile.close()
	#print quotedic
#2,4:6,8:

#getquotes(link)

links=[]
f = open("categories.csv", "rb")
reader = csv.reader(f)
for row in reader:
	links.append(row[0])

for link in links[801:805:]:
	print link
	
		getquotes(link)
	except:
		print "error loading --> "+link
#Code Tested On Ubuntu. Won't work on Windows.

import multiprocessing as mp
import csv
import urllib2
from bs4 import BeautifulSoup
import json
import csv


#get links
links=[]
f = open("categories.csv", "rb")
reader = csv.reader(f)
for row in reader:
	links.append(row[0])

## set the number for parallel execution. High number means faster and resource intensive on CPU and Memory
#eg: runs 4 parallel execution at a time, 
parts = 4
#########################

#dividing the list to equal parts for parallel execution
processarray =[]
ini=0
elements = len(links)/parts
eni= elements
for i in range(parts):
    print "ini:eni,",ini,eni
    processarray.append(links[ini:eni])
    ini = eni
    eni+=elements
    if eni > len(links):
        processarray.append(links[ini:])
        break

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


def getquotesInit(links):
    for i in links:
        try:
            getquotes(i)
        except:
            print "error while processing : "+i

# Setup a list of processes that we want to run
processes = [mp.Process(target=getquotesInit, args=(alinks,)) for alinks in processarray]

# Run processes
for p in processes:
    p.start()

# Exit the completed processes
for p in processes:
    p.join()

# Get process results from the output queue
#results1 = [output.get() for p in processes]

#print len(results1)
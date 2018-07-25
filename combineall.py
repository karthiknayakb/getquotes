import json
import os

path = "quotes\\"
#file = "Tyranny.json"

files = os.listdir(path)

combinedAll = []

for file in files:
	with open(path+file) as f:
    		data = json.load(f)
    		combinedAll = combinedAll+data

f = open(path+"combinedAll.json","w")
json.dump(combinedAll,f)
f.close()
print "all quotes ---> ",len(combinedAll)

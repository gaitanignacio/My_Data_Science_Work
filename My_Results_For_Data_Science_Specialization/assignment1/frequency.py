import sys
import json
import re

def lines(fp):
	print str(len(fp.readlines()))
def contains_word(s, w):
	return w in re.findall(r"[\w']+",s)
def main():
	tweet_file = open(sys.argv[1])
	data=[]
	freq={}

	for l in tweet_file:
		data.append(json.loads(l))

	for tweet in data:
		try:
			for x in re.findall(r"[\w']+",tweet[u'text'].encode('utf-8')):
				if x in freq:
					freq[x]=1+freq[x]
				else:
					freq[x]=1
		except KeyError:
			freq[""]=0	
	for x in freq.keys():
		if freq[x]!=0:	
			print x + " "+ str(freq[x])			
	tweet_file.close()
if __name__ == '__main__':
	main()


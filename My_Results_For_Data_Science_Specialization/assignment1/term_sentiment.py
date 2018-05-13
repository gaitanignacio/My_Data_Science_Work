import sys
import json
import re

def lines(fp):
	print str(len(fp.readlines()))
def contains_word(s, w):
	return w in re.findall(r"[\w']+",s) #(' ' + w + ' ') in (' ' + s + ' ')
def main():
	sent_file = open(sys.argv[1])
	tweet_file = open(sys.argv[2])
	
	scores = {} # initialize an empty dictionary
	terms= {}
	data = []
	sentiment=[]
	aux = 0
    
	for line in sent_file:
		term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
		scores[term] = int(score)  # Convert the score to an integer.

	for l in tweet_file:
		data.append(json.loads(l))

	for tweet in data:
		try:
			for key in scores:
				if contains_word(tweet[u'text'].encode('utf-8'),key):
					aux = aux+scores[key]
			sentiment.append([tweet[u'text'].encode('utf-8')] + [aux]) #"This is the result:",aux
			aux=0
		except KeyError:
        		sentiment.append([""] +[0]) #("This line is not a Tweet")
	
	#print sentiment[7]
	for tweet,score in sentiment:
		for x in re.findall(r"[\w']+",tweet):
			if x in terms:
				terms[x]=int(score)+terms[x]
			else:
				terms[x] = int(score)

	for x in terms.keys():
		print x +" " + str(terms[x])
	sent_file.close()
	tweet_file.close()
if __name__ == '__main__':
	main()


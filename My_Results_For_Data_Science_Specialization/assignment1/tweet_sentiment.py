import sys
import json
import re
#from pprint import pprint

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))
def contains_word(s, w):
    return w in re.findall(r"[\w']+",s)
    #return (' ' + w + ' ') in (' ' + s + ' ')
def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    #hw()
    #lines(sent_file)
    #lines(tweet_file)
    scores = {} # initialize an empty dictionary
    data = []
    for line in sent_file:
      term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
      scores[term] = int(score)  # Convert the score to an integer.
    #print scores.items() # Print every (term, score) pair in the dictionary
    for l in tweet_file:
      data.append(json.loads(l))
    #encoded_string = data[1][u'text'].encode('utf-8')
    #print encoded_string
    aux = 0
    for tweet in data:
      try:
        #print tweet[u'text'].encode('utf-8')
        for key in scores:
            if contains_word(tweet[u'text'].encode('utf-8'),key):
              aux = aux+scores[key]
              #print key
              #print scores[key]
        print aux #"This is the result:",aux
        aux=0
      except KeyError:
        print 0 #("This line is not a Tweet")
    sent_file.close()
    tweet_file.close()
if __name__ == '__main__':
    main()

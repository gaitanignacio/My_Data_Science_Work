import sys
import json
import re
#from difflib import SequenceMatcher

def contains_word(s, w):
	return w in re.findall(r"[\w']+",s)

def which_state_is(location):
	state_dic = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'}
	for ab,loc in state_dic.items():
		#if SequenceMatcher(None,loc,location)>0.8:
		for word in location.split(" "):
			if contains_word(loc,word):
				return ab
	return "NAS"
def main():
	sent_file = open(sys.argv[1])
	tweet_file = open(sys.argv[2])
	
	scores = {} # initialize an empty dictionary
	terms= {}
	data = []
	t_state_sent=[]
	state_sent={}
	aux = 0
   	happiest_state="NN" 
	for line in sent_file:
		term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
		scores[term] = int(score)  # Convert the score to an integer.

	for l in tweet_file:
		data.append(json.loads(l))

	for tweet in data:
		try:
			if tweet[u'user'][u'location'] is None:
				tweet[u'user'][u'location']=""
		except KeyError:
			aux=0
	for tweet in data:
		try:
			for key in scores:
				if contains_word(tweet[u'text'].encode('utf-8'),key):
					aux = aux+scores[key]
			t_state_sent.append([tweet[u'text'].encode('utf-8')]+ [which_state_is(tweet[u'user'][u'location'].encode('utf-8'))] + [aux]) #"This is the result:",aux
			#print tweet[u'user'][u'location']
			aux=0
		except KeyError:
        		t_state_sent.append(["NAT"]+["NAS"]+[0]) #("This line is not a Tweet")
	
	for tweet,state,score in t_state_sent:
		if state in state_sent:
			state_sent[state]=int(score)+state_sent[state]
		else:
			state_sent[state] = int(score)

	#print state_sent
	del state_sent['NAS']
	#print state_sent
	#print max(state_sent, happiest_state=lambda happiest_state: stete_sent[happiest_state])
	
	for happiest_state,happiness in state_sent.items():
		if happiness==max(state_sent.values()):
			print happiest_state
	sent_file.close()
	tweet_file.close()
if __name__ == '__main__':
	main()


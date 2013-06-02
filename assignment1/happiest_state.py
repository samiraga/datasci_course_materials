import sys
import json 
import re
import operator

state_regex = re.compile('(AL$|AK$|AZ$|AR$|CA$|CO$|CT$|DE$|DC$|FL$|GA$|HI$|ID$|IL$|IN$|IA$|KS$|KY$|LA$|ME$|MD$|MA$|MI$|MN$|MS$|MO$|MT$|NE$|NV$|NH$|NJ$|NM$|NY$|NC$|ND$|OH$|OK$|OR$|PN$|RI$|SC$|SD$|TN$|TX$|UT$|VT$|VA$|WA$|WV$|WI$|WY$)')

states = {}
terms = {}

def load_sentiment(file):
	for line in file.readlines():
		[term, sentiment] = line.split('\t')
		terms[term] = int(sentiment)

def find_happiest_state(file):
	for line in file.readlines():
		tweet = json.loads(line)

		text = tweet.get('text')
		state = get_state(tweet)

		if text and state:
			if state not in states:
				states[state] = get_sentiment(text)
			else:
				states[state] += get_sentiment(text)

	sorted_states = sorted(states.items(), key=operator.itemgetter(1), reverse=True)

	print sorted_states[0][0]


def get_sentiment(line):
	sentiment = 0.0
	for term in line.split():
		sentiment += terms.get(term, 0)

	return sentiment

def get_state(tweet):
	place = tweet.get('place')

	if place and place.get('place_type') == 'city' and place.get('country_code') == 'US' and place.get('full_name'):
		name = place.get('full_name').split()

		if state_regex.match(name[-1]):
			return name[-1]
		else:
			return None
	else:
		return None


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    load_sentiment(sent_file)
    find_happiest_state(tweet_file)

if __name__ == '__main__':
    main()
import sys
import json
import math

terms = {}
new_terms = {}

def load_sentiment(file):
	for line in file.readlines():
		[term, sentiment] = line.lower().split('\t')
		terms[term] = int(sentiment)

def process_tweets(file):
	for line in file.readlines():
		tweet = json.loads(line)
		text = tweet.get('text')

		if text:
			calc_sentiment(text.lower())

def get_sentiment(line):
	sentiment = 0.0
	for term in line.split():
		sentiment += terms.get(term, 0)

	return sentiment

def calc_sentiment(line):
	sentiment = get_sentiment(line)

	for term in line.split():
		if term not in terms:
			# init if for first time
			if term not in new_terms:
				new_terms[term] = [0, 0, 0, 0]
			
			if sentiment < 0:
				new_terms[term][0] += 1
			elif sentiment == 0:
				new_terms[term][1] += 1
			else:
				new_terms[term][2] += 1

def print_new_terms():
	for (term, freq) in new_terms.items():
		neg = freq[0]
		zero = freq[1]
		pos = freq[2]

		total = neg + zero + pos

		if neg > zero and neg > pos:
			sentiment = -5 * neg/float(total)
		elif zero >= neg and zero > pos:
			sentiment = 0
		elif pos >= neg and pos >= float(zero):
			sentiment = 5 * pos/float(total)

		freq[3] = math.ceil(sentiment)

		print "%s %f" %(term.encode('utf-8'), sentiment)

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    load_sentiment(sent_file)
    process_tweets(tweet_file)
    print_new_terms()

if __name__ == '__main__':
    main()
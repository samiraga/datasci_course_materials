import sys
import json 

terms = {}

def load_sentiment(file):
	for line in file.readlines():
		[term, sentiment] = line.split('\t')
		terms[term] = int(sentiment)

def calculate_sentiments(file):
	for line in file.readlines():
		tweet = json.loads(line)
		text = tweet.get('text')

		if text:
			print get_sentiment(text)

def get_sentiment(line):
	sentiment = 0.0
	for term in line.split():
		sentiment += terms.get(term, 0)

	return sentiment

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    load_sentiment(sent_file)

    calculate_sentiments(tweet_file)

if __name__ == '__main__':
    main()

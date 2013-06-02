import sys
import json
import operator

hashtags = {}

def count_hashtags(tweet_file):
	for line in tweet_file.readlines():
		tweet = json.loads(line)

		if tweet.get('entities'):
			tags = tweet['entities']['hashtags']

			for tag in tags:
				text = tag['text']

				if text not in hashtags:
					hashtags[text] = 1
				else:
					hashtags[text] += 1

def print_top_ten():
	sorted_tags = sorted(hashtags.items(), key=operator.itemgetter(1), reverse=True)

	for tag in sorted_tags[:10]:
		print "%s %f" % (tag[0].encode('utf-8'), tag[1])

def main():
	tweet_file = open(sys.argv[1])

	count_hashtags(tweet_file)
	print_top_ten()

if __name__ == '__main__':
	main()
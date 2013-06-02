import sys
import json

terms = {}
total = 0

def count_frequencies(file):
	global total

	for line in file.readlines():
		tweet = json.loads(line)
		text = tweet.get('text')

		if text:
			for term in text.split():
				term = term.lower().strip('.,:;<>#@!=/-+?\'\"[]\\{}()$%')

				if term not in terms:
					terms[term] = 0
				else:
					terms[term] += 1

				total += 1

def print_frequencies():
	for (term, count) in terms.items():
		print "%s %f" % (term.encode('utf-8'), count/float(total))

def main():
    tweet_file = open(sys.argv[1])

    count_frequencies(tweet_file)
    print_frequencies()

if __name__ == '__main__':
    main()

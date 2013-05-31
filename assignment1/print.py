import urllib
import json

NUM_OF_PAGES  = 10
BASE_URL      = "http://search.twitter.com/search.json"
SEARCH        = "?q=datascience"

next_page = SEARCH

while next_page != "":
  tweets = json.load(urllib.urlopen(BASE_URL + next_page))  

  current_page = tweets["page"]
  next_page = tweets.get("next_page", "")

  # Last page
  if current_page > NUM_OF_PAGES:
    next_page = ""

  for tweet in tweets["results"]:
    print tweet["text"].encode('utf-8')
import MapReduce
import json
import sys

mr = MapReduce.MapReduce()

# Map function
def mapper(record):
	doc_id = record[0]
	text = record[1]

	for word in text.split():
		mr.emit_intermediate(word, doc_id)

# Reduce function
def reducer(key, list_of_values):
	values = list(set(list_of_values))
	mr.emit((key, values))

inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)
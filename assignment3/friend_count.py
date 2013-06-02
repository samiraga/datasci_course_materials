import MapReduce
import json
import sys

mr = MapReduce.MapReduce()

# Map function
def mapper(record):
	person = record[0]
	friend = record[1]

	mr.emit_intermediate(person, 1) 

# Reduce function
def reducer(key, list_of_values):
	friends = 0
	for friend in list_of_values:
		friends += 1

	mr.emit((key, friends))

inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)
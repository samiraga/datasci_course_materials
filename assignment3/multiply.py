import MapReduce
import json
import sys

mr = MapReduce.MapReduce()

a_rows = 5
a_cols = 5

b_rows = 5
b_cols = 5

# Map function
def mapper(record):
	matrix = record[0]
	row = record[1]
	column = record[2]
	value = record[3]

	if matrix == "a":
		for b_col in xrange(0, b_cols):
			mr.emit_intermediate((row, b_col),(matrix, column, value))
	else:
		for a_row in xrange(0, a_rows):
			mr.emit_intermediate((a_row, column),(matrix, row, value))

# Reduce function
def reducer(key, list_of_values):
	a = [0]*5
	b = [0]*5

	for value in list_of_values:
		if value[0] == "a":
			a[value[1]] = value[2]
		else:
			b[value[1]] = value[2]

	sum = 0
	for x in xrange(0,5):
		sum += a[x] * b[x]

	mr.emit((key[0], key[1], sum))

inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)
import MapReduce
import json
import sys

mr = MapReduce.MapReduce()

# Map function
def mapper(record):
	label = record[0]
	order_id = record[1]

	mr.emit_intermediate(order_id, (label, record))

# Reduce function
def reducer(key, list_of_values):
	order = lines = []

	for t in list_of_values:
		if (t[0] == "order"):
			order = t[1]
		else:
			lines.append(t[1])

	for line in lines:
		output = order + line
		mr.emit(output)

inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)
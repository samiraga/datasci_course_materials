import MapReduce
import json
import sys

mr = MapReduce.MapReduce()

# Map function
def mapper(record):
	seq_id = record[0]
	nucleotides = record[1]

	trimmed_nucleotides = nucleotides[:-10]

	mr.emit_intermediate(trimmed_nucleotides, 1)

# Reduce function
def reducer(key, list_of_values):
	mr.emit(key)

inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)
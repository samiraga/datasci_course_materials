import MapReduce
import json
import sys

mr = MapReduce.MapReduce()

# Map function
def mapper(record):
	person = record[0]
	friend = record[1]

	mr.emit_intermediate(person, ("has_friend", friend))
	mr.emit_intermediate(friend, ("is_friend_of", person))

# Reduce function
def reducer(key, list_of_values):
	my_friends = set()
	i_am_friend = set()

	for friendship in list_of_values:
		friend_type = friendship[0]
		friend = friendship[1]

		if (friend_type == "has_friend"):
			my_friends.add(friend)
		else:
			i_am_friend.add(friend)

	diff = my_friends.difference(i_am_friend)
	diff2 = i_am_friend.difference(my_friends)

	for friend in diff:
		mr.emit((key, friend))

	for friend in diff2:
		mr.emit((key, friend))

inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)
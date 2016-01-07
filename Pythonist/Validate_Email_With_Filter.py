import re

n = int(raw_input())
l = []

for x in range(n) :

	l.append(raw_input())


l = list(filter (lambda x : re.match('^([a-zA-Z0-9-_]+@[a-zA-Z0-9]+[.].{,3})$', x) , l))

print sorted(l)
import re

n = int(raw_input())

for x in range(n) :

	s = raw_input()

	matchObj = re.match('^[789][0-9]{9}$', s)

	if matchObj :

		print 'YES'

	else :

		print 'NO'
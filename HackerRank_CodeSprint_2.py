n = int(raw_input())
s = raw_input()
length = len(s)
count = length
d = {}

for x in set(s) :

	d[x] = [i for i, letter in enumerate(s) if letter == x]

for x in d :

	length_of_value = len(d[x])

	if length_of_value >= 2 :

		for y in range(2, length_of_value + 1) :

			count = count + ( length_of_value - y + 1 )

print count
n, p, x = map(int, raw_input().split())
l = map(int, raw_input().split())
maximum = l[0]*p
maximum_number = 1

for z in range(1,len(l)) :

	p = p - x
	y = l[z] * p

	if y > maximum :

		maximum = y
		maximum_number = z + 1

print maximum_number
n, k = map(int, raw_input().split())
boys = map(float, raw_input().split())
girls = map(float, raw_input().split())

boys.sort()
girls.sort()

print boys
print girls

count = 0

for x in range(n) :

	z = x

	if abs( boys[x] - girls[x] ) <= float(k) :

		count = count + 1

	else :

		for y in range(x+1, n) :

			if abs( boys[y] - girls[z] ) <= float(k) :

				boys[y], boys[z] = boys[z], boys[y]
				count = count + 1
				break

print '----'
print boys
print girls

print count
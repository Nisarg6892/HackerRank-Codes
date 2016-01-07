n = int(raw_input())
l = map(int, raw_input().split())
pair = 3
final = 0

while pair <= n/2 :

	for x in range(0, n-2*pair+1) :

		z = x+pair
		first = [l[y] for y in range(x, z)]
		# print str(first)+'f'

		while z <= n - pair :
			
			second = [l[y] for y in range(z, z+pair)]

			Sum = 0

			Second_Length = len(second)

			for q in range(Second_Length) :

				Sum = Sum + ( first[q]*second[Second_Length-q-1] )

			# print str(second)+'s', Sum

			if Sum > final :

				final = Sum

			z = z + 1

	pair = pair + 1

# print final, len(final)
print final

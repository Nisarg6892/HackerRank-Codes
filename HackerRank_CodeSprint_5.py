# n = int(raw_input())
# l = []

# for x in range(n) :

# 	string_list_int = map(int, raw_input().split())

# 	l.append(string_list_int)

# print l

# for x in range(0, len(l)-1) :

# 	y = x + 1

# 	while y < n :

# 		print x
# 		print 'hi'

# 		if l[x][0] > l[y][0] and l[x][1] < l[y][1] :

# 			del l[y]
# 			y = y - 1
# 			print 'hello'

# 		y = y + 1

# print l




l = [1,2,3,4]
print l.index(1)
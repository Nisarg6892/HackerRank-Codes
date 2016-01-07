n, k = map(int, raw_input().split())
l = []

for x in range(k) :

	l.append(int(raw_input()))

# l.sort()
Full_List = range(1,9)
After_Cut = Full_List - l

print After_Cut

for x in After_Cut :

	if (x+1) in l or (x-1) in l


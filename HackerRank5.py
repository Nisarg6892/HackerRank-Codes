l=raw_input()
r=raw_input()

max=0

for x in range(int(l),int(r)+1):
	for y in range(int(x)+1,int(r)+1):
		
		if (x^y)>max:
			max=x^y
print max

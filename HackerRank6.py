TestCase=raw_input()
t=[None]*10
for x in range (0,int(TestCase)):
	t[x]=raw_input()

for i in range (0,len(t)):
	if t[i] is not None:
		count=0
		for j in range(0,len(t[i])):
			#temp=t[i][j]
			if j!=0:
				if t[i][j]==t[i][j-1]:
					count+=1
		print count

				

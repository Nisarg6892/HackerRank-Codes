TestCase=raw_input()
t=[None]*10
for x in range(0,int(TestCase)):
	t[x]=raw_input()

initial_height=1
print '-------------'

for x in range(0,len(t)):
	if t[x] is not None:
		if int(t[x])==0:
			print '1'
		elif int(t[x])==1:
			print '2'
		else:
			#print t[x]
			height_even=2*initial_height+1
			n=int(t[x])/2
			#print n
			for i in range(1,n):
				height_even=2*height_even+1
			if int(t[x])%2==0:
				print height_even
			else:
				print height_even*2

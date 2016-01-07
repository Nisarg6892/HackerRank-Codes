#n=raw_input('How many expressions do you want to enter?')
#for x in range(0,int(n)):
#	raw_input()
#exp1='11+32'
#print 'hello'
#print len(exp1)
#for x in range(0,5):
#	if x=='+':
#		print 'hi'
totalNumbers=raw_input()
a=[None]*15
for i in range(0,int(totalNumbers)):
	a[i]=raw_input()

for x in range(0,len(a)):
	if a[x] is not None:
		count=0
		for digit in str(a[x]):
			if digit=='0':
				continue
			else:
				if int(a[x])%int(digit)==0:
					count+=1
		print count
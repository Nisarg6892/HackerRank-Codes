#for i in range(0,10**10):
noOfTestCase=raw_input()
t=[None]*10**5
for x in range(0,int(noOfTestCase)):
	t[x]=raw_input()
n=[None]*100
count=0
n[0]=0
print n[0]
n[1]=1
print n[1]
#print n2
i=2
while n[i]<=10**10:
	n[i]=n[i-2]+n[i-1]
	count+=1
	if n[i]>10**10:
		break
	#print n[i]
	i+=1
#print "count=",count

for x in range(0,len(t)):
	for y in range(0,len(n)):
		if t[x]==n[y]:
			print t[x],' IsFibo'
			break

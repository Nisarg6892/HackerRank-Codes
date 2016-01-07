firstString=raw_input()
secondString=raw_input()

firstList=list(firstString)
secondList=list(secondString)
thirdList=secondList[:]

x=[]
y=[]

for i in range(0,len(firstList)):
	for j in range(0,len(secondList)):
		if firstList[i]==secondList[j]:
			x.append(firstList[i])
			secondList[j]=''
			break
print x

for i in range(0,len(thirdList)):
	for j in range(0,len(firstList)):
		if thirdList[i]==firstList[j]:
			y.append(thirdList[i])
			firstList[j]=''
			break
print y
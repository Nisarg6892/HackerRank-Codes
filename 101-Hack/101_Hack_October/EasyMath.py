import re

# n=90000
# i=0
# l=[]

# while i<n:
# 	matchObj=re.match(r'^4+0*$',str(i))

# 	if matchObj:
# 		l.append(int(format(matchObj.group())))
# 		# print format(matchObj.group())
# 		# print 'hello'
# 	i+=1

# print l
# print 'hi'

t=1
for i in range(0,t):
	
	X=40
	Y=1

	while True:

		matchObj=re.match(r'^4+0*$',str(X*Y))

		if matchObj:
			break
		else:
			Y+=1

	number=format(matchObj.group())
	four=number.count('4')
	zero=number.count('0')
	print 2*four+zero



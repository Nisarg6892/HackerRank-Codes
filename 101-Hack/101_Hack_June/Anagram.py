t=int(1)
for testcase in range(0,t):
	string='xaxbbbxx'
	string_list=list(string)
	if len(string)%2==0:
		s1=string_list[:len(string_list)/2]
		s2=string_list[(len(string_list)/2):]
		print s1,s2
		count=0
		for i in range(0,len(s1)):
			# del s1[i]
			for j in range(0,len(s2)):
				if s1[i]==s2[j]:
					count+=1
					# del s1[i]
					# del s2[j]
					s1.pop(i)
					s2.pop(j)
					break
		print s1,s2
		print len(s1)-count
	else:
		print '-1'
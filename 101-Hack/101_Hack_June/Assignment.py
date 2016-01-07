t=1
for i in range(0,t):
	string='2 9'
	string_list=string.split()
	m=int(string_list[0])
	n=int(string_list[1])

	s=''
	for digit in range(1,m+1):
		
		for i in range(1,n+1):
			# for j in range(i,n+1):
			s=str(digit)+str(i)
			print s


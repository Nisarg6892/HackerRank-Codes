t=1
for i in range(0,t):
	TotalCuts=9
	if TotalCuts%2==0:
		TotalPieces=(TotalCuts/2)*(TotalCuts/2)
		# print TotalPieces
	else:
		TotalPieces=(TotalCuts/2)*(TotalCuts/2+1)
	print TotalPieces

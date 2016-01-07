n = int(raw_input())

length = len(bin(n)[2:])

for x in range(1, n+1) :

	octal = str(oct(x))[1:]
	hexadecimal = str(hex(x))[2:]
	binary = str(bin(x))[2:]

	print (length-len(str(x)))*' '+str(x), (length-len(octal))*' '+octal, (length-len(hexadecimal))*' '+hexadecimal.upper(), (length-len(binary))*' '+binary
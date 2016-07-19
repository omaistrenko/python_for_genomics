n=10
for y in range(2, n):
	for x in range(2,y):
		if y%x==0:
			print y, 'equals', x, '*', y//x
			break
	else:
		print y, 'is a prime number'
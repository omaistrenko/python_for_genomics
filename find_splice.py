dna=raw_input('enter dna sequence:')

pos=dna.find('gt', 0) #position of donor site

while pos>-1:
	print "donor splice site candidate at position %d"%pos
	pos=dna.find('gt',pos+1)
else: print "not donor gt splice sites"
	
mot=['aaaatttt', 'dffgf', 'sgsfgg']
for m in mot:
	print m,len(m)
	
for i in range(1,10,2):
	print(i)
dna=raw_input('enter dna sequence:')

if 'n' in dna:
	nbases=dna.count('n')
	print "dna sequence has %d undentified bases" %nbases
else: 
	print "no n in this sequence"

if 'n' in dna or 'N' in dna:
	nbases=dna.count('n')+dna.count('N')
	print "dna seguece has %d undefiened bases " % nbases
	
	
mot='aattcca'
dna='aattaattcca'
print mot in dna
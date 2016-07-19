dna=raw_input("type dna sequence:")
def gc(dna):
		"this function computes the GC content of DNA sequence"
		nbases=dna.count('n')+dna.count('N')
		gcpercentage=float(dna.count('c')+dna.count('C')+dna.count('g')+dna.count('G'))*100.0/(len(dna)-nbases)
		return gcpercentage
		#print gcpercentage
		
print gc(dna)
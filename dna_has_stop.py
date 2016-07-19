dna=raw_input("type dna sequence:")

def has_stop_codon(dna):
	"this function checks if given dna sequence has frame stop codons"
	stop_codon_found=False
	stop_codons=['tga','tag', 'taa']
	for i in range(0, len(dna),3):
		codon=dna[i:i+3].lower()
		if codon in stop_codons:
			stop_codon_found=True
			break
	return stop_codon_found
if has_stop_codon(dna):
	print "sequence has stop codon"
else :
	print "sequence does not have stop codons"
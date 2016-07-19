def rev_com(seq):
	"""return reverse compl of the given dna sequence"""
	seq=reverse_string(seq)
	seq=complement(seq)
	return seq
	
def reverse_string(seq):
	return seq[::-1] #empty : returns whole string, argument -1 makes python to in oposite direction

def complement(dna):
	"""return the complementary sequence"""
	basecomplement={'A':'T', 'C':'G', 'T':'A', 'N':'N', 'a':'t', 'c':'g', 'g':'c', 't':'a', 'n':'n'}
	letters=list(dna)
	letters=[basecomplement[base]] for base in letters]
	return ''.join(letters)
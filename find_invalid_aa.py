protein='ATDFNGNSLDKDSJHFKASHGDFKAHGFKHSDJJPLMNVBHFHYQZBHDRURTPOJGBDHVCGSAFE'

for i in range(len(protein)):
	if protein[i] not in 'ABCDEFGHIKLMNPQRSTVWXYZ':
		print "protein contains invalid aminoacid %s at position %d"%(protein[i], i)

for i in range(len(protein)):
	if protein[i] not in 'ABCDEFGHIKLMNPQRSTVWXYZ':
		print "this not valid protein"
		break
		
corect_prot=''
for i in range(len(protein)):
	if protein[i] not in 'ABCDEFGHIKLMNPQRSTVWXYZ':
		continue
	corect_prot=corect_prot+protein[i]

print "corrected protein sequence is: %s" %corect_prot
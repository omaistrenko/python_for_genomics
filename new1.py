print """\
>dna1
atatatatattatatat
atatatatatat
atatatattatttta
>dna2
atttttttattttt
atattatataaa
"""

###

dna="aaaagggagaggaatttccccagctagcgctaacsss"
dna1="aaaTaTTTAACCCcGGG"
dna_count_a=dna.count('aa')
print str(dna_count_a)

DNA=dna.upper()
print str(DNA)

DNA1=dna1.upper()
print str(DNA1)

print str(dna.find('aa'))

print str(dna.replace('a','A'))

no_c=dna.count('c')
print str(no_c)
no_g=dna.count('g')
print str(no_g)
totaldna_len=len(dna)
print str(totaldna_len)
gc_perc=(no_c+no_g)*100.0/totaldna_len
print str(gc_perc) + " % of GC"





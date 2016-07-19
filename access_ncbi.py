from Bio.Blast import NCBIWWW
fasta_string = open("myseq.txt").read()
result_handle = NCBIWWW.qblast("blastn", "n", fasta_string)
print result_handle

from Bio.Blast import NCBIXML
blast_record = NCBIXML.read(result_handle)
print len(blast_record.alignments)
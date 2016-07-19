from Bio.Blast import NCBIXML
blast_record = NCBIXML.read(result_handle)
print len(blast_record.alignments)
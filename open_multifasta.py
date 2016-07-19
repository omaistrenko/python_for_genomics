try:
	f=open('multifasta.txt', 'r') #prints error if 'r' in quoets
except IOError:
	print "multifasta.txt doesn't exist"
#f=open('multifasta.txt', 'r')	
seqs={} #empty dictionary
for line in f:
	line=line.rstrip() #"discard a newline character"
	if line[0]=='>': #distiguish header from sequence ##alternative way: line.startswith('>')
		words=line.split()
		name=words[0][1:]
		seqs[name]=''
	else: #for the line that is not header
		seqs[name]=seqs[name]+line
		
print seqs
f.close()
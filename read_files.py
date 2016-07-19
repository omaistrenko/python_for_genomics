try:
	f=open('test_file.txt', 'r') #prints error if 'r' in quoets
except IOError:
	print "the file doesn't exist"
	
	
for line in f:
	print(line)

f.seek(0)
print f.read()
f.seek(0)
print f.readline()
f.close()


f=open('test_file.txt', 'a')
f.write('\ndddddddd')
f.close()
f=open('test_file.txt', 'r')

for line in f:
	print(line)
		
f.close()
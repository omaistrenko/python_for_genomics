print 'hello world'

#analog of STDN in perl
nam = raw_input('Who are you?')
print 'Welcome',nam

#convert european floors into usa
inp = raw_input('European floor?')
usf = int(inp)+1
print "US floor", usf

#hours/rate/pay
inp = raw_input("Enter Hours: ")
hours = float(inp)
inp = raw_input("Enter Rate: ")
rate = float(inp)
print rate, hours
pay = rate*hours
print pay

# Elena Chumakova
# 8.5 Open the file mbox-short.txt and read it line by line. 
# When you find a line that starts with 'From ' like the following line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# You will parse the From line using split() and print out the second word in the line 
# (i.e. the entire address of the person who sent the message). Then print out a count at the end.
# Hint: make sure not to include the lines that start with 'From:'.



import pandas as pd

x = open("mbox.txt")
# for line in x:
# 	if line.startswith('From '):
# 		l=line.split()
# 		print(l[1])
# 	else:
# 		continue

for line in x:
	line = line.rstrip()
	words = line.split()
	if len(line) > 1 and words[0]=='From':
		print(words[1])
	
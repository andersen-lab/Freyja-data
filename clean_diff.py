import sys

fn = sys.argv[1]
file1 = open(fn, 'r')
lineages = file1.readlines()
lineages = [l.strip() for l in lineages]
# drop things that were just reordered. 
newThings = []
for l in lineages:
	if '+' in l:
		if l.replace('+','-') not in lineages:
			newThings.append(l)

if len(newThings)>0:			
	print(newThings,fn)
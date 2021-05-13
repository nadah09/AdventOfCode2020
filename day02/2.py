f = open("2.txt", "r")
lines = [i.strip() for i in f]

def processLine(line):
	policy, pw = line.split(": ")
	numrange, letter = policy.split(" ")
	low, high = numrange.split("-")
	low, high = int(low), int(high)
	return low, high, letter, pw

#Part 1
def findValid(lines):
	total = 0
	for line in lines:
		low, high, letter, pw = processLine(line)
		count = pw.count(letter)
		if count >= low and count <= high:
			total += 1
	return total 

print(findValid(lines))

#Part 2 
def findValid2(lines):
	total = 0
	for line in lines:
		ind1, ind2, letter, pw = processLine(line)
		matches = sum([1 if pw[i-1] == letter else 0 for i in [ind1, ind2]])
		if matches == 1:
			total += 1
	return total

print(findValid2(lines))

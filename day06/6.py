f = open("6.txt", "r")
answers = f.read().split("\n\n")

#Part 1
def countYesInGroup(group):
	group = "".join(group.split("\n"))
	return len(set(group))

def countTotalYes(groups):
	return sum([countYesInGroup(group) for group in groups])

print(countTotalYes(answers))

#Part 2
def countYesInGroup2(group):
	group = group.split("\n")
	countsNeeded = len(group)
	group = "".join(group)
	print(group, countsNeeded, sum([1 if group.count(i) >= countsNeeded else 0 for i in set(group)]), "\n")
	return sum([1 if group.count(i) >= countsNeeded else 0 for i in set(group)])

def countTotalYes2(groups):
	return sum([countYesInGroup2(group) for group in groups])

print(countTotalYes2(answers))

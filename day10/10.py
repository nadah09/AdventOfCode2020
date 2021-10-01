f = open("10.txt", "r")
adaptors = [int(i) for i in f.read().split("\n")]

#Part 1
def findJoltDifferences(adaptors):
	counts = {1: 0, 2: 0, 3: 0}
	for i in range(len(adaptors)-1):
		diff = adaptors[i+1] - adaptors[i]
		counts[diff] += 1
	return counts[1]*counts[3]

#Part 2
def findAllConfigurations(adaptors, start = 0, memo = None):
	if not memo:
		memo = {}
	if start >= len(adaptors)-1:
		return 1
	else:
		poss = [start+1, start+2, start+3]
		currAdaptor = adaptors[start]
		sum_ = 0
		for p in poss:
			try:
				nextAdaptor = adaptors[p]
				if nextAdaptor - currAdaptor <= 3:
					if p not in memo:
						memo[p] = findAllConfigurations(adaptors, p, memo)
					sum_ += memo[p]
			except:
				pass
		return sum_
	
def findAllConfigurationsBottomUp(adaptors):
	memo = {}
	memo[0] = 1
	for i in range(1, len(adaptors)):
		poss = [i-1, i-2, i-3]
		memo[i] = 0
		for p in poss:
			if p >= 0:
				if adaptors[i] - adaptors[p] <= 3:
					memo[i] += memo[p]
	return memo[len(adaptors)-1]


adaptors = [0] + sorted(adaptors) + [max(adaptors)+3]
print(findJoltDifferences(adaptors))
print(findAllConfigurations(adaptors))
print(findAllConfigurationsBottomUp(adaptors))




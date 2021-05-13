f = open("1.txt", "r")
inputs = [int(i) for i in f]

#Part 1
def findTwoSumSet(x, total):
	seen = set(x)
	for i in seen:
		if total-i in seen:
			return i, total-i

def findSum(x, total):
	for i in x:
		twoSum = findTwoSumSet(x, total)
		try:
			return twoSum[0]*twoSum[1]
		except:
			continue

print(findSum(inputs, 2020))

#Part 2
def findTwoSumSet(x, total):
	seen = set(x)
	for i in seen:
		if total-i in seen:
			return i, total-i

def findThreeSum(x):
	seen = set()
	for i in x:
		twoSum = findTwoSumSet(x, 2020-i)
		try:
			return (twoSum[0]*twoSum[1]*i)
		except:
			continue

print(findThreeSum(inputs))

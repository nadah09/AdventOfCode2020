f = open("1.txt", "r")
inputs = [int(i) for i in f]

#Part 1
def twoSum(inputs, target = 2020):
	seen = set()
	for i in inputs:
		if target-i in seen:
			return i*(target-i)
		seen.add(i)
	return None

#Part 2
def threeSum(inputs):
	for i in range(len(inputs)):
		num = inputs[i]
		twoInputs = inputs[:i] + inputs[i+1:]
		twoS = twoSum(twoInputs, 2020-num)
		if twoS:
			return twoS*num
	return None

print(twoSum(inputs))
print(threeSum(inputs))


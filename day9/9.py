f = open("9.txt", "r")
nums = f.read().split("\n")

#Part 1 
def hasSum(nums, num):
	seen = set()
	for i in nums:
		if num-i in seen:
			return True
		seen.add(i)
	return False

def findInvalid(nums, skip = 25):
	nums = [int(i) for i in nums]
	for i in range(skip, len(nums)):
		previous = nums[i-skip:i]
		if not hasSum(previous, nums[i]):
			return nums[i]
	return 0

print(findInvalid(nums, 5))

#Part 2
def findSum(nums):
	nums = [int(i) for i in nums]
	invalid = findInvalid(nums, 25)

	s = 0
	e = 0
	cursum = nums[0]

	while True:
		if cursum < invalid:
			e += 1
			cursum += nums[e]
		elif cursum > invalid:
			cursum -= nums[s]
			s += 1
		else:
			r = nums[s:e+1]
			return min(r)+max(r)
	return 0

print(findSum(nums))
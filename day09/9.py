f = open("9.txt", "r")
nums = [int(i) for i in f.read().split("\n")]

def findFirstInvalid(nums):
	for i in range(26, len(nums)):
		window = nums[i-26:i]
		curr = nums[i]
		if not twoSum(window, curr):
			return curr
	return 0

def twoSum(window, target):
	seen = set()
	for i in window:
		if target-i in seen and i != target-i:
			return True
		seen.add(i)
	return False

def findSum(nums):
	target = findFirstInvalid(nums)
	l = 0
	r = 0
	curr = 0
	while curr != target:
		if curr < target:
			r += 1
			curr += nums[r-1]
		if curr > target:
			l += 1
			curr -= nums[l-1]
	window = nums[l:r+1]
	return min(window) + max(window)

print(findFirstInvalid(nums))
print(findSum(nums))
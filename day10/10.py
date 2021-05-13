f = open("10.txt", "r")
nums = f.read().split("\n")

print(nums)

#Part 1
def findJolts(nums):
	nums = [0]+sorted([int(i) for i in nums])
	ones = 0
	threes = 0
	for i in range(len(nums)-1):
		if nums[i] + 1 == nums[i+1]:
			ones+=1
		if nums[i]+3 == nums[i+1]:
			threes += 1
	return ones*(threes+1)

print(findJolts(nums))




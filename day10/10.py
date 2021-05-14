f = open("10.txt", "r")
nums = f.read().split("\n")


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

#Part 2
def findCombs(nums):
    combinations = {}
    nums = sorted([int(i) for i in nums])
    end = max(nums)+3
    nums = [0] + nums + [end]

    combinations[nums[-1]] = 1

    for value in nums[::-1]:
        if value != end:
	        sums = 0
	        for i in range(1, 4):
	            next_value = value + i
	            if next_value in nums:
	                sums += combinations[next_value]
	        combinations[value] = sums
    return combinations[0]

print(findCombs(nums))




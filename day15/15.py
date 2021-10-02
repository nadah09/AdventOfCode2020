f = open("15.txt", "r")
lines = f.read().split("\n")
print(lines)
nums = [int(i) for i in lines[0].split(",")]
print(nums)

#Part 1
def find2020Num(nums, target):
    turn = 1
    memo = {}
    currnum = nums[0]
    prev = None
    while turn < target:
        prev = currnum
        if turn < len(nums):
            currnum = nums[turn]
        else:
            if currnum in memo:
                currnum = turn - memo[currnum]
            else:
                currnum = 0
        memo[prev] = turn
        turn += 1 
    return currnum

#Part 2
#Same as Part 1


print(find2020Num(nums, 2020))
print(find2020Num(nums, 30000000))
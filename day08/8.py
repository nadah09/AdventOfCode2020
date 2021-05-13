f = open("8.txt", "r")
insts = f.read().split("\n")

#Part 1 
def findInfiniteLoop(insts):
	seen = set()
	i = 0
	acc = 0
	while i not in seen:
		if i >= len(insts):
			return acc, 1
		inst, num = insts[i].split(" ")
		num = int(num)
		seen.add(i)
		if inst == "nop":
			i += 1
		if inst == "acc":
			acc += num 
			i += 1
		if inst == "jmp":
			i += num
	return acc, 0

print(findInfiniteLoop(insts)[0])

#Part 2
def fix(insts):
	for i in range(len(insts)):
		inst, num = insts[i].split(" ")
		if inst == "jmp":
			copy = [j for j in insts]
			copy[i] = "nop" + " " + num
			acc, finished = findInfiniteLoop(copy)
			if finished == 1:
				return acc
		elif inst == "nop":
			copy = [j for j in insts]
			copy[i] = "jmp" + " " + num
			acc, finished = findInfiniteLoop(copy)
			if finished == 1:
				return acc
	return 0

print(fix(insts))





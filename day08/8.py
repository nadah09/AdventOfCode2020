f = open("8.txt", "r")
insts = f.read().split("\n")

#Part 1
def findInfiniteLoop(insts):
	acc = 0
	seen = set()
	i = 0
	while i not in seen:
		if i == len(insts):
			return True, acc
		seen.add(i)
		command, val = insts[i].split(" ")
		if command == "nop":
			i += 1
		elif command == "acc":
			acc += int(val)
			i += 1
		elif command == "jmp":
			i += int(val)
	return False, acc

#Part 2
def correctInfiniteLoop(insts):
	for i in range(len(insts)):
		inst = insts[i]
		command, val = inst.split(" ")
		if command == "nop":
			insts[i] = "jmp " + val
			fixed, acc = findInfiniteLoop(insts)
			if fixed:
				return acc
			insts[i] = "nop " + val
		elif command == "jmp":
			insts[i] = "nop " + val
			fixed, acc = findInfiniteLoop(insts)
			if fixed:
				return acc
			insts[i] = "jmp " + val
	return 0

print(findInfiniteLoop(insts)[1])
print(correctInfiniteLoop(insts))






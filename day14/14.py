f = open("14.txt", "r")
lines = f.read().split("\n")[:-1]
#print(lines)

#Part 1
def sumMemory(lines):
    memo = {}
    mask = "X"*36
    for line in lines:
        step, val = line.split(" = ")
        if step == "mask":
            mask = val
        else:
            idx = step[4:-1]
            val = modifyVal(val, mask)
            memo[idx] = val
    return sum(memo.values())

def modifyVal(val, mask):
    val = bin(int(val))[2:]
    val = [i for i in "0"*(36-len(val)) + val]
    for i in range(len(val)):
        if mask[i] != "X":
            val[i] = mask[i]
    val = int("".join(val), 2)
    return val

#Part 2
def sumMemory2(lines):
    memo = {}
    mask = "0"*36
    for line in lines:
        step, val = line.split(" = ")
        if step == "mask":
            mask = val
        else:
            idx = step[4:-1]
            memo = addVals(memo, idx, val, mask)
    return sum(memo.values())

def addVals(memo, idx, val, mask):
    idx = bin(int(idx))[2:]
    forks = []
    idx = [i for i in "0"*(36-len(idx)) + idx]
    for i in range(len(idx)):
        if mask[i] == "1":
            idx[i] = "1"
        elif mask[i] == "X":
            forks.append(i)
    results = [idx]
    for i in forks:
        curr = [j for j in results]
        for r in curr:
            poss = [r[:i] + ['0'] + r[i+1:], r[:i] + ['1'] + r[i+1:]]
            for p in poss:
                if p not in results:
                    results.append(p)
    for r in results:
        r = int("".join(r), 2)
        memo[r] = int(val)
    return memo

print(sumMemory(lines))
print(sumMemory2(lines))
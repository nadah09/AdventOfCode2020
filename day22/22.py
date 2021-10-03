f = open("22.txt", "r")
p1, p2 = f.read().split("\n\n")
p1 = [int(i) for i in p1.split("\n")[1:]]
p2 = [int(i) for i in p2.split("\n")[1:]]

#Part 1
def findWinner(p1, p2):
    while p1 and p2:
        c1 = p1.pop(0)
        c2 = p2.pop(0)
        if c1 > c2:
            p1.append(c1)
            p1.append(c2)
        else:
            p2.append(c2)
            p2.append(c1)
    if not p1:
        return findScore(p2)
    if not p2:
        return findScore(p1)

def findScore(p):
    score = 0
    for i in range(len(p)):
        score += (i+1)*p[-i-1]
    return score

#Part 2
def findWinner2(p1, p2):
    seen = set()
    while p1 and p2:
        config = "p1"+",".join([str(i) for i in p1])+"p2"+",".join([str(i) for i in p2])
        if config in seen:
            p2 = []
            break
        else:
            seen.add(config)
        c1 = p1.pop(0)
        c2 = p2.pop(0)
        if c1 <= len(p1) and c2 <= len(p2):
            p1copy = [p1[i] for i in range(c1)]
            p2copy = [p2[i] for i in range(c2)]
            winner, _ = findWinner2(p1copy, p2copy)
            if winner == "p1":
                p1.append(c1)
                p1.append(c2)
            else:
                p2.append(c2)
                p2.append(c1)
        else:
            if c1 > c2:
                p1.append(c1)
                p1.append(c2)
            else:
                p2.append(c2)
                p2.append(c1)
    if not p1:
        return "p2",findScore(p2)
    if not p2:
        return "p1", findScore(p1)

p1copy = [i for i in p1]
p2copy = [i for i in p2]

print(findWinner(p1, p2))
print(findWinner2(p1copy, p2copy))
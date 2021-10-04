f = open("23.txt", "r")
cups = [int(i) for i in f.read()]
print(cups)

#Part 1
def iterate100(cups):
    current = 0
    for _ in range(100):
        current, cups = simulate(current, cups)
    
    start = cups.index(1)
    cups = cups[start+1:]+cups[:start]
    return "".join([str(i) for i in cups])
    
def simulate(current, cups):
    removeInds = [1, 2, 3]
    remove = [cups[(current+i)%len(cups)] for i in removeInds]
    currVal = cups[current]
    d = cups[current]-1
    cups = [i for i in cups if i not in remove]
    if d < min(cups):
        d = max(cups)
    if d in remove and d-1 in remove and d-2 in remove:
        d = d-3
    while d in remove:
        d -= 1
        if d < min(cups):
            d = max(cups)
    indD = cups.index(d)
    cups = cups[:indD+1] + remove + cups[indD+1:]
    return (cups.index(currVal)+1)%len(cups), cups


print(iterate100(cups))
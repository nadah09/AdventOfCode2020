f = open("20.txt", "r")
tiles = f.read().split("\n\n")
numToEdges = {}
for t in tiles:
    edges = []
    lines = t.split("\n")
    name = lines[0].split(" ")[1][:-1]
    edges.append(lines[1])
    edges.append(lines[-1])
    edges.append("".join([i[0] for i in lines[1:]]))
    edges.append("".join([i[-1] for i in lines[1:]]))
    numToEdges[int(name)] = edges

#Part 1 
def findCorners(numToEdges):
    numToMatches = {}
    product = 1
    for edge in numToEdges:
        numToMatches[edge] = countMatches(numToEdges, edge)
        if numToMatches[edge] == 2:
            product*=edge
    return product


def countMatches(numToEdges, num):
    edgesToMatch = numToEdges[num]
    count = 0
    for edge in edgesToMatch:
        seen = False
        for nums in numToEdges:
            if nums != num:
                for e in numToEdges[nums]:
                    if e == edge or e == edge[::-1]:
                        seen = True
        if seen:
            count += 1
    return count

print(findCorners(numToEdges))




f = open("7.txt", "r")
bags = f.read().split("\n")

#Part 1
def makeGraph(bags):
	childToParent = {}
	parentToChild = {}
	for bag in bags:
		parent, children = bag.split(" contain ")
		parent = ' '.join(parent.split(" ")[:2])
		children = [i.split(" bag")[0].strip() for i in children.split(", ")]
		for child in children:
			num, color = child.split(" ")[0], " ".join(child.split(" ")[1:])
			try:
				childToParent[color].append(parent)
			except:
				childToParent[color] = [parent]
			try:
				num = int(num)
				try:
					parentToChild[parent].append((color, num))
				except:
					parentToChild[parent] = [(color, num)]
			except:
				continue
	return childToParent, parentToChild

def BFS(graph, start):
	queue = [start]
	seen = set()
	while queue:
		curr = queue.pop(0)
		seen.add(curr)
		if curr in graph:
			for parent in graph[curr]:
				queue.append(parent)
	return len(seen)-1

def findPossibleBags(bags, start):
	graph, parentToChild = makeGraph(bags)
	return BFS(graph, start)


#Part 2
def DFS(parentToChild, start):
	if start in parentToChild:
		sum_ = 1
		for color, num in parentToChild[start]:
			sum_ += int(num)*DFS(parentToChild, color)
		return sum_
	else:
		return 1

def findTotalBags(bags, start):
	graph, parentToChild = makeGraph(bags)
	return DFS(parentToChild, start)-1
	

print(findPossibleBags(bags, "shiny gold"))
print(findTotalBags(bags, "shiny gold"))


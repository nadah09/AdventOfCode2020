f = open("7.txt", "r")
bags = f.read().split("\n")

#Part 1
def make_parent_dict(bags):
	parents = {}
	childrenDict = {}
	for bag in bags:
		parse = bag.split(" contain ")
		parent = parse[0].split(" bags")[0]
		children = parse[1:]
		children = children[0].strip().split(", ")
		for child in children:
			child = child.split(" ")
			number = child[0]
			color = child[1]+" "+child[2]
			if color == "other bags.":
				parents[parent] = []
			elif color != None:
				try:
					parents[parent].append((number, color))
				except:
					parents[parent] = [(number, color)]
				try:
					childrenDict[color].append(parent)
				except:
					childrenDict[color] = [parent]
	return parents, childrenDict

def BFS(bags):
	_, children = make_parent_dict(bags)
	start = "shiny gold"
	final = []
	queue = [start]
	seen = set()
	while queue:
		curr = queue.pop(0)
		if curr != start:
			final.append(curr)
		if curr in children:
			for child in children[curr]:
				queue.append(child)

	return len(set(final))

print(BFS(bags))

#Part 2
def DFS(bags, bag_type, parents = []):
	if not parents:
		parents, _ = make_parent_dict(bags)
	return sum(int(num) * DFS(bags, typ, parents) for num, typ in parents[bag_type]) + 1


print(DFS(bags, "shiny gold")-1)


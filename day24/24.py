f = open("24.txt", "r")
tiles = f.read().split("\n")

#Part 1
def countBlackTiles(tiles):
    seen = set()
    for tile in tiles:
        coord = findCoord(tile)
        add = False
        if coord not in seen:
            add = True
        if add:
            seen.add(coord)
        else:
            seen.remove(coord)
    return len(seen)
        

def findCoord(tile):
    i = 0
    coord = [0, 0]
    while i < len(tile):
        d = tile[i]
        if d == "e":
            coord[0] += 2
        elif d == "w":
            coord[0] -= 2
        else:
            d = tile[i:i+2]
            if d[0] == "n":
                coord[1] += 1
            else:
                coord[1] -= 1
            if d[1] == "e":
                coord[0] += 1
            else:
                coord[0] -= 1
            i+= 1
        i+=1
    return (coord[0], coord[1])

#Part 2
def findFloor(tiles):
    seen = set()
    for tile in tiles:
        coord = findCoord(tile)
        add = False
        if coord not in seen:
            add = True
        if add:
            seen.add(coord)
        else:
            seen.remove(coord)
    return seen

def flip(floor):
    toRemove = set()
    toAdd = set()
    xs = [i[0] for i in floor]
    ys = [i[1] for i in floor]
    for x in range(min(xs)-2, max(xs)+3):
        for y in range(min(ys)-2, max(ys)+3):
            black = findBlack(x, y, floor)
            if (x, y) not in floor and black == 2:
                toAdd.add((x, y))
            if (x, y) in floor and (black == 0 or black >2):
                toRemove.add((x, y))
    for r in toRemove:
        floor.remove(r)
    for a in toAdd:
        floor.add(a)
    return floor

    return floor

def findBlack(x, y, floor):
    count = 0
    neighbors = [(x+2, y), (x-2, y), (x+1, y+1), (x-1, y-1), (x+1, y-1), (x-1, y+1)]
    for n in neighbors:
            if n in floor:
                count += 1
    return count


def flip100(tiles):
    floor = findFloor(tiles)
    for i in range(100):
        floor = flip(floor)
    return len(floor)

print(countBlackTiles(tiles))
print(flip100(tiles))
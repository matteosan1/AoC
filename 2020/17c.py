class Cube:
    def __init__(self):
        self.status = False
        self.neighbours = []
        self.buffer = False

    def add_neighbour(self, cube):
        if cube not in self.neighbours:
            self.neighbours.append(cube)

    def buffer_update(self):
        if self.status:
            self.buffer = [cube.status for cube in self.neighbours].count(True) in [2, 3]
        else:
            self.buffer = [cube.status for cube in self.neighbours].count(True) == 3

    def commit(self):
        self.status = self.buffer


def neighbours_p1(location):
    neighbours = []
    for x in [location[0] - 1, location[0], location[0] + 1]:
        for y in [location[1] - 1, location[1], location[1] + 1]:
            for z in [location[2] - 1, location[2], location[2] + 1]:
                if x == location[0] and y == location[1] and z == location[2]:
                    continue
                neighbours.append((x, y, z))
    return neighbours


def neighbours_p2(location):
    neighbours = []
    for x in [location[0] - 1, location[0], location[0] + 1]:
        for y in [location[1] - 1, location[1], location[1] + 1]:
            for z in [location[2] - 1, location[2], location[2] + 1]:
                for w in [location[3] - 1, location[3], location[3] + 1]:
                    if x == location[0] and y == location[1] and z == location[2] and w == location[3]:
                        continue
                    neighbours.append((x, y, z, w))
    return neighbours


def go(p1=True):
    cubes = {}
    z = 0
    w = 0
    for row, line in enumerate(open('input_17a.txt')):
        line = line.strip()
        for col, char in enumerate(line):
            if char == '.':
                continue
            else:
                location = (row, col, z) if p1 else (row, col, z, w)
                if location not in cubes:
                    cubes[location] = (Cube())
                cube = cubes[location]
                cube.status = True
                neighbours = neighbours_p1((row, col, z)) if p1 else neighbours_p2((row, col, z, w))
                for neighbour in neighbours:
                    cubes[neighbour] = Cube() if neighbour not in cubes else cubes[neighbour]
                    cube.add_neighbour(cubes[neighbour])
                    cubes[neighbour].add_neighbour(cube)

    for _ in range(6):
        for cube in cubes.values():
            cube.buffer_update()
        for cube in cubes.values():
            cube.commit()

        # Update all active cubes with neighbours:
        active_cubes = [(location, cube) for location, cube in cubes.items() if cube.status]
        for location, cube in active_cubes:
            neighbours = neighbours_p1(location) if p1 else neighbours_p2(location)
            for neighbour in neighbours:
                cubes[neighbour] = Cube() if neighbour not in cubes else cubes[neighbour]
                cube.add_neighbour(cubes[neighbour])
                cubes[neighbour].add_neighbour(cube)

    return sum([1 for cube in cubes.values() if cube.status])


print(f"Part 1 Answer: {go(p1=True)}")
print(f"Part 2 Answer: {go(p1=False)}")

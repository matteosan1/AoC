import numpy as np

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    GREY = '\033[0;37;40m'
    BLACK = '\033[0;30;40m'
    RED = '\033[0;31;40m'
    GREEN = '\033[0;32;40m'
    YELLOW = '\033[0;33;40m'
    BLUE = '\033[0;34;40m'
    PURPLE = '\033[0;35;40m'
    CYAN = '\033[0;36;40m'
    WHITE = '\033[0;37;40m'
    
#	No effect	0	Black	40
#	Bold	1	Red	41
#	Underline	2	Green	42
#	Negative1	3	Yellow	43
#	Negative2	5	Blue	44
#			Purple	45
#			Cyan	46

def readInput(filename):
    lines = []
    with open(filename) as f:
        for l in f:
            if l.lstrip() == "":
                continue
            lines.append(l.split("\n")[0])
    return lines

def readInputWithBlank(filename):
    lines = []
    with open(filename) as f:
        for l in f:
            lines.append(l.split("\n")[0])
    return lines

def printArray(cm, points=None, color=bcolors.OKGREEN):
    if points is None:
        for y in range(cm.shape[1]):
            for x in range(cm.shape[0]):
                print (int(cm[x, y]), end="")
            print ("")
    else:
        points = list(map(tuple, points))
        for y in range(cm.shape[1]):
            for x in range(cm.shape[0]):
                if (x,y) in points:
                    print (color + str(int(cm[x, y])) + bcolors.ENDC, end="")
                else:
                    print (bcolors.GREY + str(int(cm[x, y])) + bcolors.ENDC, end="")
            print ("")

def printMap(cm):
    for y in range(cm.shape[1]):
        for x in range(cm.shape[0]):
            if cm[x, y] == 0:
                print (".", end="")
            else:
                print (bcolors.BOLD+"#"+bcolors.ENDC, end="")
        print ("")
    print ("\n")

def printPath(cm, paths, start, end):
    path = [end]
    pos = end
    neighs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    xmax = paths.shape[0]
    ymax = paths.shape[1]
    while pos != start:
        neis = [(pos[0] + n[0], pos[1] + n[1]) for n in neighs if 0 <= pos[0]+n[0] < xmax and 0 <= pos[1]+n[1] < ymax]
        minimum = np.inf
        p = None
        for n in neis:
            #print ("n ", n)
            if n != path[-1] and paths[(n[0], n[1])] < minimum:
                p = n
                minimum = paths[(n[0], n[1])]
        pos = p
        path.append(p)

    printArray(cm, path, bcolors.BOLD)

class Point:
    def __init__(self, x, y, typ=0, edge=0):
        self.x = x
        self.y = y
        self.prev = None
        self.g = 0
        self.h = 0
        self.f = 0
        self.edge = edge
        self.next = []
        self.next2 = {}
        self.typ = typ

    def distance(self, other):
        return np.sqrt((self.x-other.x)**2 + (self.y-other.y)**2)
        
    def mod(self):
        return np.sqrt(self.x**2 + self.y**2)

    def __hash__(self):
        return hash((self.x, self.y))
    
    def __lt__(self, other):
        return self.mod() < other.mod()

    def __ge__(self, other):
        return self.mod() >= other.mod()

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __neq__(self, other):
        return self.x != other.x and self.y != other.y

    def __add__(self, other):
        return Point(self.x+other.x, self.y+other.y)

    def __sub__(self, other):
        return Point(self.x-other.x, self.y-other.y)

    def __repr__(self):
        return f"({self.x},{self.y})"
        
def manhattan_dist(p1, p2):
    return abs(p1.x-p2.x) + abs(p1.y-p2.y)

def shoelace(vertices):
    A = 0
    for i in range(len(vertices)):
        if i == len(vertices)-1:
            A += vertices[i].x*vertices[0].y - vertices[i].y*vertices[0].x
        else:
            A += vertices[i].x*vertices[i+1].y - vertices[i].y*vertices[i+1].x
    return abs(A//2)
    
def perimeter(vertices):
    P = 0
    for i in range(len(vertices)):
        if i == len(vertices)-1:
            P += manhattan_dist(vertices[i],vertices[0])
        else:
            P += manhattan_dist(vertices[i],vertices[i+1])
    return P
    
def hex_to_rgb(value):
    return tuple(int(value[i:i+2], 16) for i in (0, 2, 4))
    
def convert_to_coordinates(lines, start_symb="@", end_symb="X"):
    m = {}
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if lines[y][x] == "#":
                continue
            c = Point(x, y)
            if lines[y][x] == start_symb:
                start = c
                c.edge = 1
            elif lines[y][x] == end_symb:
                end = c
                c.edge = 1
            elif lines[y][x] == " ":
                c.edge = 1
            else:
                c.edge = int(lines[y][x])
            m[c] = c
    return m, start, end

def readMap(path):
    lines = []
    with open(path, "r") as f:
        for l in f.readlines():
            lines.append(l.rstrip())
    return convert_to_coordinates(lines)

dirs = {0:lambda c:c + Point(0,1),
        1:lambda c:c + Point(1,0),
        2:lambda c:c + Point(0,-1),
        3:lambda c:c + Point(-1,0),}

full_dirs = {0:lambda c:c + Point(0,1),
             1:lambda c:c + Point(1,1),
             2:lambda c:c + Point(0,1),
             3:lambda c:c + Point(1,-1),
             4:lambda c:c + Point(0,-1),
             5:lambda c:c + Point(-1,-1),
             6:lambda c:c + Point(-1,0),
             7:lambda c:c + Point(-1,1),}

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def tail(self):
        if self.head is None:
            return None
        current = self.head
        while True:
            n = current.next
            if n is None:
                return current
            else:
                current = n
        
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    def after(self, node, data):
        if node is None:
            raise ValueError("Node must be nonnull")
        new_node = Node(data)
        new_node.prev = node
        new_node.next = node.next
        if node.next:
            node.next.prev = new_node
        node.next = new_node

    def before(self, node, data):
        if node is None:
            raise ValueError("Node must be nonnull")
        new_node = Node(data)
        new_node.prev = node.prev
        new_node.next = node
        if node.prev:
            node.prev.next = new_node
        if new_node.prev is None:
            self.head = new_node
        node.prev = new_node

    def length(self):
        l = 0
        cur_node = self.head
        while cur_node:
            l += 1
            cur_node = cur_node.next
        return l

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

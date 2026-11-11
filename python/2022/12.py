from utils import readInput
        
class Graph:
    def __init__(self, graph_dict=None):
        if graph_dict is None:
            graph_dict = {}
        self.graph_dict = graph_dict

    def edges(self, vertice):
        return self.graph_dict[vertice]

    def all_vertices(self):
        return set(self.graph_dict.keys())

    def all_edges(self):
        return selg.generate_edges()

    def add_vertex(self, vertex):
        if vertex not in self.graph_dict:
            self.graph_dict[vertex] = []

    def add_edge(self, edge):
        v1, v2 = tuple(set(edge))
        for x, y in [(v1, v2), (v2, v1)]:
            self.graph_dict.setdefault(x, []).append(y)

    def generate_edges(self):
        edges = []
        for v in self.graph_dict:
            for neighbour in self.graph_dict[v]:
                edges.append((v, neighbour))
                edges.append((neighbour, v))
        return edges

    def __iter__(self):
        self._iter_obj = iter(self.graph_dict)
        return self._iter_obj

    def __next__(self):
        return next(self._iter_obj)

    def __str__(self):
        res = "vertices: "
        for k in self.graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.generate_edges():
            res += str(edge) + " "
        return res

    def find_path(self, start, end, path=None):
        if path is None:
            path = []
        graph = self.graph_dict
        path = path + [start]
        if start == end:
            return path
        if start not in graph:
            return None
        for v in graph[start]:
            if v not in path:
                extended_path = self.find_path(v, end, path)
                if extended_path:
                    return extended_path
        return None

    def find_all_paths(self, start, end, path=[]):
        graph = self.graph_dict
        path = path + [start]
        if start == end:
            return [path]
        if start not in graph:
            return []
        paths = []
        for vertex in graph[start]:
            insert = False
            if (vertex == vertex.lower() and vertex not in path):
                insert = True
            elif vertex != vertex.lower():
                insert = True
            if insert:
                extended_paths = self.find_all_paths(vertex, end, path)
                for p in extended_paths:
                    paths.append(p)
        return paths

    def small_caves(self):
        small = []
        for k in self.graph_dict:
            if k == "start" or k == "end":
                continue
            if k == k.lower():
                small.append(k)
        return small

    def find_special_paths(self, start, end):
        small = self.small_caves()
        graph = self.graph_dict
        super_paths = []

        for i, s in enumerate(small):
            print ("{}/{}".format(i, len(small)))
            paths = self.find_all_paths2(s, start, end)
            for p in paths:
                if p not in super_paths:
                    super_paths.append(p)
            #break
        return super_paths

    def find_all_paths2(self, cave, start, end, path=[]):
        graph = self.graph_dict
        path = path + [start]
        if start == end:
            return [path]
        if start not in graph:
            return []
        paths = []
        for vertex in graph[start]:
            insert = False
            if (vertex == cave and path.count(cave) < 2):
                insert = True
            if (vertex == vertex.lower() and vertex not in path):
                insert = True
            elif vertex != vertex.lower():
                insert = True
            if insert:
                extended_paths = self.find_all_paths2(cave, vertex, end, path)
                for p in extended_paths:
                    paths.append(p)
                    
        return paths

g = Graph()
edges = readInput("input_12.txt")
for edge in edges:
    e = edge.split("-")
    g.add_edge(e)

paths = g.find_all_paths("start", "end")
#print (p)
print ("🎄 Part 1: {}".format(len(paths)))

paths = g.find_special_paths("start", "end")
print ("🎄🎅 Part 2: {}".format(len(paths)))


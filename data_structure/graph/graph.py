from vertex import Vertex
class Graph:
    def __init__(self, directed=False, dict = None):
        self.graph_dict = {}
        self.directed = directed
        if dict is not None:
            directed = self.directed
            self.directed = True
            self.from_dict(dict)
            self.directed = directed

    def add_vertex(self, vertex):
        self.graph_dict[vertex.value] = vertex

    def add_edge(self, from_vertex, to_vertex, weight=0):
        self.graph_dict[from_vertex.value].add_edge(to_vertex.value, weight)
        if not self.directed:
            self.graph_dict[to_vertex.value].add_edge(
                from_vertex.value, weight)

    def find_path(self, start_vertex, end_vertex):
        start = [start_vertex]
        seen = {}
        while len(start) > 0:
            current_vertex = start.pop(0)
            seen[current_vertex] = True
            print("Visiting " + current_vertex)
            if current_vertex == end_vertex:
                return True
            else:
                vertices_to_visit = set(
                    self.graph_dict[current_vertex].edges.keys())
                start += [vertex for vertex in vertices_to_visit if vertex not in seen]
        return False

    def from_dict(self, dict):
        for key in dict.keys():
            key = Vertex(key)
            self.add_vertex(key)

        for key, item in dict.items():
            key = self.graph_dict[key]
            for vertex in item:
                vertex = self.graph_dict[vertex]
                self.add_edge(key, vertex)
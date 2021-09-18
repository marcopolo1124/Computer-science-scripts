from graph import Graph
def bfs(graph, start_vertex, target_value):
    path = [start_vertex]
    bfs_queue = [path]
    visited = set()
    while bfs_queue:
        path = bfs_queue.pop(0)
        current_vertex = path[-1]
        visited.add(current_vertex)
        for neighbor in graph.graph_dict[current_vertex].edges.keys():
            if neighbor not in visited:
                if neighbor is target_value:
                    return path + [neighbor]

                else:
                    bfs_queue.append(path + [neighbor])

dict = {
    'lava': set(['sharks', 'piranhas']),
    'sharks': set(['lava', 'bees', 'lasers']),
    'piranhas': set(['lava', 'crocodiles']),
    'bees': set(['sharks']),
    'lasers': set(['sharks', 'crocodiles']),
    'crocodiles': set(['piranhas', 'lasers'])
  }

the_most_dangerous_graph = Graph(directed = True, dict = dict)


# Call dfs() below and print the result:
print(bfs(the_most_dangerous_graph,'crocodiles', 'bees'))

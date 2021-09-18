from graph import Graph
from vertex import Vertex

def dfs(graph, current_vertex, target_value, visited=[]):
	
  visited.append(current_vertex)
  
  if current_vertex == target_value:
    return visited
	
  # Add your recursive case here:
  for neighbor in graph.graph_dict[current_vertex].edges.keys():
    if neighbor not in visited:
      path = dfs(graph, neighbor, target_value, visited)
      if path:
        return path
  return None



dict = {
    'lava': set(['sharks', 'piranhas']),
    'sharks': set(['lava', 'bees', 'lasers']),
    'piranhas': set(['lava', 'crocodiles']),
    'bees': set(['sharks']),
    'lasers': set(['sharks', 'crocodiles']),
    'crocodiles': set(['piranhas', 'lasers'])
  }

the_most_dangerous_graph = Graph(directed = True, dict = dict)

print(the_most_dangerous_graph.graph_dict)

# Call dfs() below and print the result:
print(dfs(the_most_dangerous_graph,'crocodiles', 'bees'))

print(the_most_dangerous_graph.graph_dict['lava'].edges)
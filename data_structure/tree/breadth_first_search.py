from collections import deque
from tree_node import TreeNode

root = TreeNode('A')
branch_b = TreeNode('B')
branch_c = TreeNode('C')
root.add_child(branch_b, branch_c)

branch_b1 = TreeNode('B1')
branch_b2 = TreeNode('B2')
branch_c1 = TreeNode('C1')
branch_c2 = TreeNode('C2')

branch_b.add_child(branch_b1, branch_b2)
branch_c.add_child(branch_c1, branch_c2)

# Breadth-first search function
def bfs(root_node, goal_value):

  # initialize frontier queue
  path_queue = deque()

  # add root path to the frontier
  initial_path = [root_node]
  path_queue.appendleft(initial_path)
  
  # search loop that continues as long as
  # there are paths in the frontier
  while path_queue:
    # get the next path and node 
    # then output node value
    current_path = path_queue.pop()
    current_node = current_path[-1]
    print(f"Searching node with value: {current_node.value}")

    # check if the goal node is found
    if current_node.value == goal_value:
      return current_path

    # add paths to children to the  frontier
    for child in current_node.children:
      new_path = current_path.copy()
      new_path.append(child)
      path_queue.appendleft(new_path)

  # return an empty path if goal not found
  return None

print(bfs(root, 'B'))
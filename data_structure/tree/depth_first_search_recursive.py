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

def dfs(root, target, path=()):
  path = path + (root,)

  if root.value == target:
    return path

  for child in root.children:
    path_found = dfs(child, target, path)

    if path_found is not None:
      return path_found

  return None

path = dfs(root, 'A')
print(path)
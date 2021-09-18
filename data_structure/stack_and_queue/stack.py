from node import Node

class Stack:
  def __init__(self, name, limit=1000):
    self.top_item = None
    self.size = 0
    self.limit = limit
    self.name = name

  def get_name(self):
    return self.name
  def get_size(self):
    return self.size
  def print_items(self):
    lst = []
    current = self.top_item
    while current:
      lst.insert(0,current.get_value())
      current = current.next_node
    return lst


  def push(self, value):
    if self.has_space():
      item = Node(value)
      item.set_next_node(self.top_item)
      self.top_item = item
      self.size += 1
  def pop(self):
    if not self.is_empty():
      item_to_remove = self.top_item
      self.top_item = item_to_remove.get_next_node()
      self.size -= 1
      return item_to_remove.get_value()

  def peek(self):
    if not self.is_empty():
      return self.top_item.get_value()

  def has_space(self):
    return self.limit > self.size

  def is_empty(self):
    return self.size == 0
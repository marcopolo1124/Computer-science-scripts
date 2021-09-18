class Node:
    """
    An object for storing a single node of a linked list.
    Models two attributes - data and the link to the next node in the list
    """

    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node data: %s>" % self.data


class LinkedList:
    """
    Singly linked list
    """

    def __init__(self):
        self.head = None

    def lst_to_link(self, lst):
        for i in range(len(lst)):
            lst[i] = Node(lst[i])

        for i in range(len(lst)):
            if i != len(lst) - 1:
                lst[i].next_node = lst[i+1]
        self.head = lst[0]

    def is_empty(self):
        """
        Returns whether the linked list is empty or not
        """
        return self.head == None

    def size(self):
        """
        Returns the number of nodes in the list.
        Take O(n) time
        """
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node

        return count

    def add(self, data):
        """
        Adds new Node containing data at the head of the list
        Takes constant time
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):
        """
        Search for the first node containing data that matches the key
        Return the node or 'None' if not found
        """
        current = self.head
        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None

    def insert(self, data, index):
        """
        Inserts a new Node containing data at index position
        Insertion take O(1) time but finding the node at the
        insertion point takes O(n) time.

        Takes overall O(n) time
        """
        new = Node(data)
        if index == 0:
            self.add(new)

        if index > 0:
            position = index
            current = self.head
            while position > 1:
                current = current.next_node
                position -= 1

            prev_node = current
            next_node = current.next_node

            prev_node.next_node = new
            new.next_node = next_node

    def append(self, data):
        size = self.size()
        if size > 0:
            self.insert(data, size)
        if size == 0:
            self.head = Node(data)

    def delete(self, index):
        """
        Removes the node at the index position
        """
        if index == 0:
            self.head = self.head.next_node
        else:
            current = self.head
            position = index
            while position > 1:
                current = current.next_node
                position -= 1

            prev_node = current
            next_node = current.next_node.next_node

            prev_node.next_node = next_node

    def delete_by_key(self, key):
        """
        Removes node containing data that matches the key
        Takes O(n) time
        """

        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current == self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node
        return current

    def __iter__(self):
        self.current_node = self.head
        return self

    def __next__(self):
        if self.current_node is not None:
            return_val = self.current_node
            self.current_node = self.current_node.next_node
            return return_val
        else:
            raise StopIteration

    def __getitem__(self, index):
        current = self.head
        if isinstance(index, int):
            current = self.head
            if index == 0:
                return self.head
            if index > 0:
                for i in range(index):
                    if current is not None:
                        current = current.next_node
                    else:
                        raise IndexError('Index out of range')

            if current is None:
                raise IndexError('Index out of range')
            else:
                return current

        if isinstance(index, slice):
            start, stop, step = index.indices(self.size())
            current = self.head
            if start == 0:
                head = self.head
            else:
                for i in range(start):
                    current = current.next_node
                head = current

            new_linked_lst = LinkedList()
            new_head = Node(head.data)
            new_linked_lst.head = new_head
            for i in range(start, stop - 1, step):
                for j in range(step):
                    current = current.next_node
                new_linked_lst.append(current.data)

            return new_linked_lst

    def __repr__(self):
        nodes = []
        current = self.head
        while current:
            if current is self.head:
                nodes.append("[Head:%s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail:%s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)

            current = current.next_node
        return '->'.join(nodes)


ll1 = LinkedList()
ll1.append(10)
print(ll1)

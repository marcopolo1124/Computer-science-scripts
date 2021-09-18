from linked_list import LinkedList

def merge_sort(linked_list):
    """
    Sorts a linked list in ascending order
    - Recursively divide the linked list into sublists containing a single node
    - Repeatedly merge the sublists to produce sorted sublists until one remains

    Returns a sorted linked list
    """

    if linked_list.size() == 1 or linked_list.head is None:
        return linked_list

    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left,right)

def split(linked_list):
    """
    Divide the unsorted list at midpoint into sublists
    """
    midpoint = linked_list.size()//2
    return linked_list[:midpoint], linked_list[midpoint:]

def merge(left, right):
    """
    Merges two lists, sorting them in the process
    Returns a new merged list

    Runs in O(n) time
    """

    l = LinkedList()
    i = 0
    j = 0

    while i<left.size() and j<right.size():
        left_i = left[i]
        right_j = right[j]
        if left_i.data < right_j.data:
            
            l.append(left_i.data)
            i+=1
        else:
            l.append(right_j.data)
            j+=1

    while i < left.size():
        
        l.append(left[i].data)
        i+=1

    while j < right.size():
        l.append(right[j].data)
        j+=1
    return l
    
ll1 = LinkedList()
ll1.lst_to_link([11,2,3,1,1213,3,3,1,4,5,168,687,64,1,2,3,4])
print(ll1)
sorted_ll1 = merge_sort(ll1)
print(sorted_ll1)
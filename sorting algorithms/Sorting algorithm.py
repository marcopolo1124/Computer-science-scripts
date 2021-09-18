import time
import random
from verify_sorted import verify_sorted

def split_list(lst):
    """
    Divide the unsorted list at midpoint into sublists
    Returns two sublists - left and right
    Takes O(log(n)) time
    """
    length = len(lst)
    midpoint = length//2

    left = lst[:midpoint]
    right = lst[midpoint:]
    return left,right

   
def merge(left, right):
    """
    Merges two lists, sorting them in the process
    Returns a new merged list

    Runs in O(n) time
    """

    l = []
    i = 0
    j = 0

    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i+=1
        else:
            l.append(right[j])
            j+=1

    while i < len(left):
        l.append(left[i])
        i+=1

    while j < len(right):
        l.append(right[j])
        j+=1
    return l
    
def merge_sort(lst):
    """
    Sorts a list in ascending order
    Returns a new sorted list

    Divide: Find the midpoint of the list and divide into sublists
    Conquer: Recursively sort the sublists created in previous step
    Combine: Merge the sorted sublists created in previous step

    Overall sorting time is O(nlog(n))
    """
    if len(lst) <= 1:
        return lst



    left_lst, right_lst = split_list(lst)
    left = merge_sort(left_lst)
    right = merge_sort(right_lst)

    return merge(left, right)


lst = [random.randint(0, 1000) for i in range(50)]

print(lst)


start_merge = time.time()
sorted_list = merge_sort(lst)
end_merge = time.time()
print('The speed of merge sort is', end_merge - start_merge)
print('Sorted?', verify_sorted(sorted_list))
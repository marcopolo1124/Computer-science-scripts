import random
import time
from verify_sorted import verify_sorted

def quicksort(list):
    if len(list) <= 1:
        return list
    left = []
    right = []
    choice = random.choice(list)
    pivot = list.pop(list.index(choice))


    for i in range(len(list)):
        if list[i] < pivot:
            left.append(list[i])
        else:
            right.append(list[i])
    

    left = quicksort(left)
    right = quicksort(right)
    left.append(pivot)
    new = left + right
    return new



lst = [random.randint(0,10000) for i in range(10000)]
lst1 = lst.copy()
lst1.sort()
print(lst)
start = time.time()
sorted_lst = quicksort(lst)
end = time.time()
print(lst1)
print(lst1 == sorted_lst)
print('The time it took for quicksort is', end - start)
print('Sorted?', verify_sorted(sorted_lst))
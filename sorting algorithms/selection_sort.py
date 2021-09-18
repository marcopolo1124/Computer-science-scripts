import random
def selection_sort(lst):
    copy = lst.copy()
    new_lst = []
    for i in range(len(copy)):
        minimum = copy[0]
        min_index = 0
        print(len(copy))
        for i in range(len(copy)):
            if copy[i] < minimum:
                minimum = copy[i]
                min_index = i
        
        new_lst.append(copy.pop(min_index))
    return new_lst

selection_sort([random.randint(0,1000)] * 10)
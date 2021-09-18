def linear_search(lst, value):
    step = 0
    for index in range(len(lst)):
        step += 1
        if lst[index] == value:
            return index
    return False
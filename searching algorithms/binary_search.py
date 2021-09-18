def binary_search(lst, value, value_index = None, step = 0):
    midpoint = len(lst)//2
    length = len(lst)
    step += 1
    # print('Length of list is', len(lst))
    if value_index is None:
        value_index = midpoint
        # print('start', value_index)

    if length == 0:
        # print(value_index)
        return False
    else:
        if lst[midpoint] == value:
            # print('Found',value_index)
            print('It took', step, 'steps')
            return value_index
        elif lst[midpoint] > value:
            value_index -= -(-midpoint//2)
            # print('decrease',value_index)
            return binary_search(lst[:midpoint], value, value_index, step)
        elif lst[midpoint] < value:
            value_index += ((length - 1) - midpoint)//2 + 1
            # print('increase',value_index)
            return binary_search(lst[midpoint+1:], value, value_index, step)

def verify(lst, func):
    for item in lst:
        print('Testing', item)
        if lst.index(item) != func(lst, item):

            print('The search result is incorrect at', item)
            return False
    print('All is fine')
    return True

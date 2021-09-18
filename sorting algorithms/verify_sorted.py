def verify_sorted(lst):
    for i in range(len(lst)):
        if i < len(lst) - 1:
            if lst[i] > lst[i+1]:
                return False
    return True

def compare(lst1, lst2):
    for i in range(len(lst1)):
        if lst1[i] != lst2[i]:
            print(i)
            return False
    return True
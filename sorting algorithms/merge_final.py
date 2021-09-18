def merge_sort(list):
    width = 1
    length = len(list)
    while width < length:
        for i in range(0, length , 2*width):
            left_start_ind = i
            left_end_ind = min(i+width, length)
            right_start_ind = min(i+width, length)
            right_end_ind = min(i + 2*width, length)

            left_length = left_end_ind - left_start_ind
            right_length = right_end_ind - right_start_ind

            list = merge(list, left_start_ind, left_end_ind, right_start_ind, right_end_ind, left_length, right_length)
        width *= 2

    return list


def merge(list, left_start, left_end, right_start, right_end, left_length, right_length):
    i = left_start
    j = right_start
    k = 0
    new_list = [0] * (left_length + right_length)

    while i < left_end and j  < right_end:
        if list[i] < list[j]:
            new_list[k] = list[i]
            i += 1
            k += 1
        else:
            new_list[k] = list[j]
            j += 1
            k+=1

    while i < left_end:
        new_list[k] = list[i]
        i+=1
        k+=1
        
    while j < right_end:
        new_list[k] = list[j]
        j+=1
        k+=1

    for l in range(left_length + right_length):
        list[left_start + l] = new_list[l]
    return list
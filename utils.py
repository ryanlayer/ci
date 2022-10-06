def find_mean(A):
    return 2

def linear_search(list_to_search, key):
    '''
    Inputs:
        list_to_search: unorderd list of values
        key: value of interest
    Returns:
        the index of the key
    '''
    for i in range(len(list_to_search)):
        curr_item = list_to_search[i]
        if key == curr_item:
            return i
    return -1


def index_list(input_list):
    '''
    Inputs:
        input_list
    Returns:
        index of list to index [(key, i), ...]
    '''
    indexed_list = []

    i = 0
    for field in input_list:
        indexed_list.append([field, i])
        i += 1
    indexed_list.sort(key=lambda tup: tup[0])
    return indexed_list


def binary_search(list_to_search, key):
    '''
    Inputs:
        list_to_search: index of dataset
        key: value of interest
    Returns:
        the index of the key
    '''
    lo = -1
    hi = len(list_to_search)
    while (hi - lo > 1):
        mid = (hi + lo) // 2

        if key == list_to_search[mid][0]:
            return list_to_search[mid][1]

        if (key < list_to_search[mid][0]):
            hi = mid
        else:
            lo = mid
    return -1

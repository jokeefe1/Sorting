# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arr1, arr2 ):
    sorted_array = []
    i, j = 0, 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            sorted_array.append(arr1[i])
            i += 1
        else:
            sorted_array.append(arr2[j])
            j += 1
        print(sorted_array)

    while i < len(arr1):
        sorted_array.append(arr1[i])
        i += 1
    while j < len(arr2):
        sorted_array.append(arr2[j])
        j += 1

    return sorted_array


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    if len(arr) < 2:
            print(f'{arr[:]}')
            return arr[:]
    else:
        middle = len(arr) // 2
        l1 = merge_sort(arr[:middle])
        l2 = merge_sort(arr[middle:])
        return merge(l1, l2)


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr

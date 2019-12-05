l = [ 8, 4, 2, 6, 7, 0]

# TO-DO: implement the Insertion Sort function below
def insertion_sort( arr ):
    for index in range(1, len(arr)):
        while index > 0 and arr[index] < arr[index -1]:
            arr[index], arr[index - 1] = arr[index - 1], arr[index]
            index -= 1
            print(arr)

    return arr

# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    spot_marker = 0
    while spot_marker <= len(arr):
        for index in range(spot_marker, len(arr)):
            if arr[index] < arr[spot_marker]:
                arr[index], arr[spot_marker] = arr[spot_marker], arr[index]
                print(arr)
        spot_marker += 1

    return arr

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    swap_happened = True
    while swap_happened:
        swap_happened = False
        for index in range(len(arr) -1):
            if arr[index] > arr[index + 1]:
                swap_happened = True
                arr[index], arr[index + 1] = arr[index + 1], arr[index]
                print(arr)
    return arr

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr



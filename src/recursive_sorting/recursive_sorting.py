# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    if elements <=2:
        return
    merged_arr = [0] * elements

    pivot = merged_arr[elements/2]
    left = []
    right = []

    for element in merged_arr:
        if element <= pivot:
            left.append(element)
        elif element > pivot:
            right.append(element)

    merged_arr = merge(left, []) + merge(right, [])
    
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO

    return arr


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

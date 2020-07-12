def partition(arr, start, end):
    # starting value is the pivote
    pivote_element = arr[start]
    iter_to_swap = start
    for iter_to_compare in range(start+1, end+1):
        if arr[iter_to_compare] < pivote_element:
            iter_to_swap += 1
            arr[iter_to_swap], arr[iter_to_compare] = arr[iter_to_compare], arr[iter_to_swap]
    arr[iter_to_swap], arr[start] = arr[start], arr[iter_to_swap]
    return iter_to_swap

def quick_sort(arr, start, end):
    if start < end:
        pivote_element_index = partition(arr, start, end)
        quick_sort(arr, start, pivote_element_index-1)
        quick_sort(arr, pivote_element_index+1, end)
        
arr = [54, 26, 93, 17, 77, 31, 44, 44, 0, -1, 4.3, 55]
quick_sort(arr, 0, len(arr)-1)
print(arr)

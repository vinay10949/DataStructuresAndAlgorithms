def selection_sort(arr):
    for each_index in range(len(arr)):
        min_index = each_index
        for iter_to_com in range(min_index, len(arr)):
            if arr[min_index] > arr[iter_to_com]:
                min_index = iter_to_com
        arr[min_index], arr[each_index] = arr[each_index], arr[min_index]
        
arr = [4,6,7,9,0,-2,9.4]
selection_sort(arr)
print(arr)
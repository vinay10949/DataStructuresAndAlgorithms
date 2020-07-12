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

'''
Class	Sorting algorithm
Data structure	Array
Worst-case performance	О(n^2) comparisons, О(n) swaps
Best-case performance	О(n^2) comparisons, O(1) swaps
Average performance	О(n2) comparisons, О(n) swaps
Worst-case space complexity	O(1) auxiliary

'''
'''
Worst-case performance	O ( n + k )  O(n+k), where k is the range of the non-negative key values.
Worst-case space complexity	O ( n + k )  O(n+k)
'''
def countingSort(arr):
    max_ele = max(arr)
    n = len(arr)
    
    result = [0]*n
    count = [0]*(max_ele+1)

    # Store the count of each elements in count array
    for i in range(0, n):
        count[arr[i]] += 1

    # Store the cummulative count
    for i in range(1, max_ele+1):
        count[i] += count[i - 1]

    # Find the index of each element of the original array in count array
    # place the elements in output array
    i = n - 1
    while i >= 0:
        result[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
        i -= 1

    # Copy the sorted elements into original array
    for i in range(0, n):
        arr[i] = result[i]
        
arr = [4, 2, 2, 5, 3, 3, 1]
countingSort(arr)
print(arr)

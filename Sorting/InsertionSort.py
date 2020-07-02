#Worst-case performance	О(n2) comparisons and swaps
#Best-case performance	O(n) comparisons, O(1) swaps
#Average performance	О(n2) comparisons and swaps
#Worst-case space complexity	О(n) total, O(1) auxiliary


def insertionSort(arr): 
    for i in range(1, len(arr)): 
        k = arr[i] #k is to be inserted at proper place
        j = i-1
        while j >=0 and k < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = k 
    return arr

arr = [12, 11, 13, 5, 6] 
arr=insertionSort(arr) 
print ("Sorted array is: ", arr) 




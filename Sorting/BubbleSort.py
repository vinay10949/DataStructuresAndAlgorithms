#Time Complexity Worst Case o(n*n-1)-- o(n^2) 
# BestCase o(n) & o(1) swaps

#Space complexity o(1)



#For first iteration n-1 comparisons and swaps

#For the second iteration n-2 comparisons and swaps.  

def bubbleSort(arr): 
    n = len(arr) 
    for i in range(n): 
        # Last i elements are already in place 
        for j in range(0, n-i-1): 
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
  
# Driver code to test above 
arr = [60, 30, 20, 10, 22, 11, 90] 
  
bubbleSort(arr) 
  
print ("Sorted array is:") 
for i in range(len(arr)): 
    print ("%d" %arr[i]),  
class PriorityQueue :
    def heapify(self, arr, n, i):
        largest=i
        left = 2*i + 1
        right = 2*i +2
        
        if left < n and arr[left] > arr[i]  :
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right 
        
        if i != largest:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr,n, largest)
        
    def buildAHeap(self, arr, n):
        for i in range(n//2,-1,-1):
            self.heapify(arr, n, i)
            
    def maxEle(self,arr):
        return arr[0]
        
    def exatractMaxEle(self,arr):
        ele = arr[0]
        arr[0] = arr[n-1]
        arr.pop()
        self.heapify(arr, len(arr), 0)
        return ele
        
    def insert(self,arr, ele):
        arr.append(ele)
        n=len(arr)
        newindex= n-1
        print(arr)
        
        parent = (newindex-1)//2 # just reverse calculation of 2i*1
        while parent >= 0:
            print("parent", parent)
            if arr[newindex] > arr[parent] :
                self.heapify(arr, n, parent)
            newindex = parent
            parent = (parent-1)//2        
        
    def increaseKey(self, arr, ele, update):
        currindex = arr.index(ele)
        n=len(arr)
        if currindex is not None and update-ele >0 : #current should not be none and update ele should lead to increase rather decrease
            arr[currindex] =  arr[currindex]+ update
            parent = (currindex-1)//2
            while parent >= 0:                
                self.heapify(arr, n, parent)
                parent = (parent-1)//2
            
pq = PriorityQueue()
arr= [4,1,3,2,16,9,10,14,8,7]
n=len(arr)
pq.buildAHeap(arr, n)

pq.insert(arr, 15)

pq.increaseKey(arr, 4,13)

print("Final arr is : " , arr)

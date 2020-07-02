def reverse(arr,a,b):
    while(a<=b):
        temp=arr[a]
        arr[a]=arr[b]
        arr[b]=temp
        a+=1
        b-=1
        
        
def rotateKtimes(arr,n,k):
    reverse(arr,n-k,n-1)
    reverse(arr,0,n-k-1)
    reverse(arr,0,n-1)
    print(arr)
    
if __name__=='__main__':
    arr=[1,2,3,4,5,6,7]
    rotateKtimes(arr,len(arr),3)


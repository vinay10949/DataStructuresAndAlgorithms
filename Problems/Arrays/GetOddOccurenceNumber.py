# Any number XOR same number is 0 ,else 1
def getOddOccurence(arr):
    res=0
    for i in arr:
        res=res^i
    return res

if __name__=='__main__':
    arr=[2, 3, 5, 4, 5, 2, 4, 3, 5, 2, 4, 4, 2]
    print(getOddOccurence(arr))

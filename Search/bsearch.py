def bSearch(arr,element,l,r):
    mid = l + ((r - l + 1) // 2);
    if(l <= r):
        if element == arr[mid] :
            return mid
        elif element < arr[mid] :
            return bSearch(arr,element,l,mid-1)
        else :
            return bSearch(arr,element,mid+1,r)
    return -1

arr = list(map(int,input("Enter array elements(inceeasing order): ").split()))
element = int(input("Enter element to be searched : "))
pos = bSearch(arr,element,0,len(arr))
if pos < 0:
    print("Element not found")
else :
    print("Element found at position ",pos+1)

def lSearch(arr,element) :
    for i in range(len(arr)) :
        if arr[i] == element :
            return i
    return -1

arr = list(map(int,input("Enter array elements : ").split()))
element = int(input("Enter element to be searched : "))
pos = lSearch(arr,element)
if pos == -1 :
    print("Element not found")
else :
    print("Element found at position ",pos+1)
